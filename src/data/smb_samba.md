---
service: samba
port: [139, 445]
cve: "CVE-2007-2447, CVE-2017-7494"
severity: critical
---
# Samba / SMB Security

## Samba "username map script"
- **CVE:** CVE-2007-2447
- **Descripción:** Ejecución remota de comandos debido a una entrada no saneada en el mapeo de usuarios.
- **Herramienta:** Metasploit (`exploit/multi/samba/usermap_script`).

## SambaCry (Samba 3.x-4.x)
- **CVE:** CVE-2017-7494
- **Descripción:** Carga de librerías compartidas maliciosas (.so) en shares con permisos de escritura.
- **Herramienta:** Metasploit (`exploit/linux/samba/is_known_pipename`).
