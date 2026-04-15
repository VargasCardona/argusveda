---
service: remote_access
port: [512, 513, 1524, 5900]
cve: "CVE-1999-0114, CVE-2006-2369"
severity: critical
---
# Remote Access & Shells

## Bindshell (Backdoor)
- **Puerto:** 1524
- **Descripción:** Una shell de root directa que no requiere autenticación. Es un "malware" histórico dejado intencionalmente.
- **Herramienta:** `nc <IP> 1524`.

## VNC (Weak Password)
- **CVE:** CVE-2006-2369 (Protocolo 3.3)
- **Descripción:** El servicio VNC usa la contraseña `password` por defecto.
- **Herramienta:** `vncviewer <IP>:5900` o Metasploit (`scanner/vnc/vnc_login`).

## R-Services (Rsh/Rlogin)
- **Puerto:** 512, 513
- **Descripción:** Servicios de ejecución remota basados en confianza de IPs. A menudo permiten acceso sin password si el archivo `.rhosts` está mal configurado.
- **Herramienta:** `rsh` o `rlogin` desde un cliente Linux.
