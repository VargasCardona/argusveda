from dotenv import load_dotenv

from .scanner import fast_triage, target_selector_chain, deep_scan
from .ingest import ingest_vulnerabilities, export_to_pdf
from .chain import full_pipeline
from .core.config import NETWORK_SCAN_RANGE

load_dotenv()

banner = """
 ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓██████▓▒░ 
 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░       ░▒▓█▓▒▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒▒▓███▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓█▓▒▒▓█▓▒░░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ ░▒▓█▓▓█▓▒░ ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░   ░▒▓██▓▒░  ░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
"""

print(banner)


def main():
    print("[ARGUSVEDA] Sistema de análisis de vulnerabilidades iniciado.")

    network_range = input(
        f"[ARGUSVEDA] Introducir rango de red objetivo [{NETWORK_SCAN_RANGE}]: "
    ).strip()
    if not network_range:
        network_range = NETWORK_SCAN_RANGE

    print(f"[ARGUSVEDA] Rango configurado: {network_range}")
    print("[ARGUSVEDA] Cargando base de conocimientos...")

    retriever = ingest_vulnerabilities()

    print("[ARGUSVEDA] Iniciando reconocimiento de superficie de ataque...")
    nmap_result = fast_triage(network_range)

    print("[ARGUSVEDA] Evaluando vectores de compromiso potenciales...")
    selected_ip = target_selector_chain.invoke({"scan_data": nmap_result})

    print(f"[ARGUSVEDA] Objetivo prioritario identificado: {selected_ip.strip()}")
    deep_scan_result = deep_scan(selected_ip)

    print("\n[ARGUSVEDA] Procesando inteligencia de vulnerabilidades...")
    resultado = full_pipeline(deep_scan_result, retriever)

    print("\n[ARGUSVEDA] ░▒▓ INFORME DE ANÁLISIS ▓▒░")
    print("=" * 60)
    print(resultado["reporte"])

    export_to_pdf(resultado["reporte"])
    print("\n[ARGUSVEDA] Análisis completado. Sesión terminada.")


if __name__ == "__main__":
    main()
