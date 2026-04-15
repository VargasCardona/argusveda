---
service: misc
port: [1099, 2049, 6667]
cve: "CVE-2010-2075, CVE-2013-1768"
severity: critical
---
# Miscellaneous Services

## UnrealIRCd (Backdoor)
- **CVE:** CVE-2010-2075
- **Descripción:** La versión instalada contiene un backdoor que se activa enviando el string `AB;` seguido de comandos al servidor IRC.
- **Herramienta:** Metasploit (`exploit/unix/irc/unreal_ircd_3281_backdoor`).

## Java RMI Registry
- **CVE:** CVE-2013-1768
- **Descripción:** El registro RMI permite la carga de clases remotas, lo que facilita la ejecución de código arbitrario.
- **Herramienta:** Metasploit (`exploit/multi/misc/java_rmi_server`).

## NFS (Network File System)
- **Puerto:** 2049
- **Descripción:** Shares de red exportados con `no_root_squash`, permitiendo a un atacante montar el sistema de archivos y leer/escribir archivos de root.
- **Herramienta:** `showmount -e <IP>` y luego `mount`.
