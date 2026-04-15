from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from ..core.llm import llm


selector_prompt = ChatPromptTemplate.from_template("""
Analiza el siguiente escaneo de red local:
{scan_data}

Tu objetivo es identificar la IP que tiene más probabilidades de ser la máquina mas vulnnerable.
Busca pistas como:
- Gran cantidad de puertos abiertos (21, 22, 23, 25, 80, 445, 3306, 5432).
- MAC addresses asociadas a VirtualBox o VMware.

Responde ÚNICAMENTE con la dirección IP encontrada. Si no estás seguro, elige la que tenga más servicios activos.
""")

target_selector_chain = selector_prompt | llm | StrOutputParser()
