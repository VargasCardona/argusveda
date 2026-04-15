---
service: databases
port: [3306, 5432]
cve: "CVE-2012-2122, CVE-2007-3280"
severity: high
---
# Database Services Security

## MySQL 5.0.51a (Password Bypass)
- **CVE:** CVE-2012-2122
- **Descripción:** Vulnerabilidad de autenticación que permite entrar como root mediante fuerza bruta rápida de errores de hash (1 de cada 256 intentos suele funcionar).
- **Herramienta:** `mysql -u root -p -h <IP>` (bucle manual) o Metasploit.

## PostgreSQL 8.3 (Weak Passwords)
- **CVE:** N/A (Configuración)
- **Descripción:** Por defecto, el usuario `postgres` suele tener la contraseña `postgres`. Permite ejecución de comandos mediante `COPY FROM PROGRAM`.
- **Herramienta:** Metasploit (`exploit/linux/postgres/postgres_payload`).
