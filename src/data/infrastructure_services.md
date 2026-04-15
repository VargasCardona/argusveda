---
service: infrastructure
port: [22, 23, 25, 53, 111]
cve: "CVE-2018-15473, CVE-1999-0613"
severity: medium
---
# Core Infrastructure Services

## OpenSSH 4.7p1 (User Enumeration)
- **CVE:** CVE-2018-15473
- **Descripción:** Fuga de información que permite saber si un usuario existe en el sistema.
- **Herramienta:** `ssh-audit` o Metasploit (`auxiliary/scanner/ssh/ssh_enumusers`).

## SMTP Postfix (VRFY)
- **CVE:** CVE-1999-0613
- **Descripción:** El comando VRFY permite enumerar usuarios reales del sistema operativo.
- **Herramienta:** `smtp-enum-users` (Nmap script).
