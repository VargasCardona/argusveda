import subprocess

from ..core.config import NETWORK_SCAN_RANGE


def fast_triage(network_range: str = None) -> str:
    if network_range is None:
        network_range = NETWORK_SCAN_RANGE

    print(f"[+] Executing initial reconnaissance on {network_range}...")

    result = subprocess.run(
        ["nmap", "--top-ports", "10", network_range], capture_output=True, text=True
    )

    print("[+] Surface reconnaissance complete. Analyzing results...")
    return result.stdout
