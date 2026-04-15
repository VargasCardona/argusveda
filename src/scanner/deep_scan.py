import subprocess


def deep_scan(target_ip: str) -> str:
    ip = target_ip.strip()

    print(f"[ARGUSVEDA] Iniciando análisis profundo de {ip}...")

    result = subprocess.run(["nmap", "-sV", "-T4", ip], capture_output=True, text=True)

    if not result.stdout:
        return f"Error: No se pudo obtener información detallada de {ip}"

    return result.stdout
