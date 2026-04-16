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
print(
    "                           by VargasCardona ~ autonomous reconnaissance on your network"
)
print(
    "                                                       v1.0.0\n"
)



def main():
    print("[+] Vulnerability analysis system initialized.")

    network_range = input(
        f"[+] Enter target network range [{NETWORK_SCAN_RANGE}]: "
    ).strip()
    if not network_range:
        network_range = NETWORK_SCAN_RANGE

    print(f"[+] Network range configured: {network_range}")
    print("[+] Loading knowledge base...")

    retriever = ingest_vulnerabilities()

    print("[+] Initiating attack surface reconnaissance...")
    nmap_result = fast_triage(network_range)

    print("[+] Evaluating potential compromise vectors...")
    selected_ip = target_selector_chain.invoke({"scan_data": nmap_result})

    print(f"[+] Priority target identified: {selected_ip.strip()}")
    deep_scan_result = deep_scan(selected_ip)

    print("\n[+] Processing vulnerability intelligence...")
    resultado = full_pipeline(deep_scan_result, retriever)

    print("\n[+] ░▒▓ ANALYSIS REPORT ▓▒░")
    print("=" * 60)
    print(resultado["reporte"])

    export_to_pdf(resultado["reporte"])
    print("\n[+] Analysis complete. Session terminated.")


if __name__ == "__main__":
    main()
