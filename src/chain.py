from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from .scanner import fast_triage, target_selector_chain, deep_scan
from .core.llm import llm


def extract_services(nmap_report: str) -> list[str]:
    extraction_prompt = ChatPromptTemplate.from_template("""
Eres un asistente técnico de ciberseguridad. 
Tu tarea es extraer UNICAMENTE los nombres de servicio y sus versiones de este reporte de Nmap.

REPORTE DE NMAP:
{nmap_raw}

INSTRUCCIONES:
1. Ignora los puertos cerrados.
2. Formatea cada elemento como 'SERVICIO VERSION' (ejemplo: 'vsftpd 2.3.4').
3. No añadas explicaciones, solo devuelve la lista separada por comas.
4. Si no hay versión, pon solo el nombre del servicio.
5. No pongas el nombre del protocolo o del puerto

LISTA DE SERVICIOS:
""")

    extraction_chain = extraction_prompt | llm | StrOutputParser()
    resultado_servicios = extraction_chain.invoke({"nmap_raw": nmap_report})
    lista_servicios = [s.strip() for s in resultado_servicios.split(",")]

    return lista_servicios


def build_context(lista_servicios: list[str], retriever) -> str:
    from .ingest.pipeline import create_retriever

    if retriever is None:
        retriever = create_retriever()

    contexto_acumulado = []
    vistos = set()

    print(f"[ARGUSVEDA] Consultando base de datos de vulnerabilidades conocidas...")
    print(f"[ARGUSVEDA] Servicios detectados: {lista_servicios}")

    for servicio in lista_servicios:
        if len(servicio) < 3 or servicio.lower() == "tcpwrapped":
            continue

        docs = retriever.invoke(servicio)

        for d in docs:
            if d.page_content not in vistos:
                contexto_acumulado.append(d.page_content)
                vistos.add(d.page_content)

    print(
        f"[ARGUSVEDA] {len(contexto_acumulado)} exposiciones identificadas. Preparando análisis..."
    )

    return "\n\n".join(contexto_acumulado)


def generate_report(inputs: dict) -> dict:
    prompt_informe = ChatPromptTemplate.from_template("""
Eres ArgusVeda una herramienta experta en ciberseguridad y pentesting. 
Tu misión es redactar un informe de vulnerabilidades basado en hallazgos de Nmap.

SERVICIOS DETECTADOS: 
{servicios}

INFORMACIÓN TÉCNICA DE REFERENCIA:
{contexto}

TAREA:
1. Analiza los servicios y busca coincidencias en la información de referencia.
2. Genera un reporte estructurado:
   - Resumen ejecutivo.
   - Detalle por servicio (Puerto, Vulnerabilidad, CVE, Severidad).
   - Comandos recomendados para explotar o verificar (Metasploit, nmap scripts, etc).
3. Si un servicio no aparece en la referencia, menciónalo brevemente como 'requiere investigación adicional'.
""")

    informe_chain = prompt_informe | llm

    return informe_chain.invoke(
        {"servicios": inputs["servicios"], "contexto": inputs["contexto"]}
    )


SCAN_CHAIN = (
    RunnableLambda(fast_triage) | target_selector_chain | RunnableLambda(deep_scan)
)


def full_pipeline(nmap_result: str, retriever=None) -> dict:
    lista_servicios = extract_services(nmap_result)
    contexto = build_context(lista_servicios, retriever)
    reporte = generate_report({"servicios": lista_servicios, "contexto": contexto})

    return {
        "servicios": lista_servicios,
        "contexto": contexto,
        "reporte": reporte.content,
    }
