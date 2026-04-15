---
service: http
port: [80, 8180]
cve: "CVE-2012-1823, CVE-2009-3548"
severity: high
---
# Web & Middleware Security

## PHP-CGI RCE (Apache 80)
- **CVE:** CVE-2012-1823
- **Descripción:** Permite pasar argumentos a la línea de comandos de PHP a través de la URL.
- **Herramienta:** Metasploit (`exploit/multi/http/php_cgi_arg_injection`).

## Apache Tomcat (Manager)
- **CVE:** CVE-2009-3548
- **Descripción:** Acceso al panel de administración con credenciales por defecto (`tomcat:tomcat`).
- **Herramienta:** Metasploit (`exploit/multi/http/tomcat_mgr_deploy`) tras obtener acceso.
