---
service: ftp
port: [21, 2121]
cve: "CVE-2011-2523, CVE-2011-1473"
severity: critical
---
# FTP Vulnerabilities

## vsftpd 2.3.4 (Backdoor)
- **CVE:** CVE-2011-2523
- **Descripción:** Un backdoor introducido en el código fuente permite acceso root si se envía un nombre de usuario terminado en `:)`.
- **Herramienta:** Metasploit (`exploit/unix/ftp/vsftpd_234_backdoor`).

## ProFTPD 1.3.1 (Mod_delay)
- **CVE:** CVE-2011-1473
- **Descripción:** Permite ataques de denegación de servicio (DoS) o fuerza bruta mediante el manejo de retardos.
- **Herramienta:** `ftp-brute` (Nmap script) o Metasploit.
