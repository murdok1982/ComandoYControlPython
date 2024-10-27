# ComandoYControlPython
# Panel de Control C2 en Python

Este es un programa de **Command and Control (C2)** básico implementado en Python. El panel permite a los operadores conectarse y gestionar sesiones de múltiples clientes de forma remota, enviar comandos y monitorear el estado de las conexiones activas. Este programa es exclusivamente para fines educativos y de pruebas de seguridad en entornos controlados y éticos.

## Características

- Acepta múltiples conexiones de clientes simultáneamente.
- Permite enviar comandos a sesiones específicas.
- Muestra un listado de todas las sesiones activas y permite seleccionar una sesión por ID.
- Incluye una interfaz de operador sencilla para gestionar las conexiones.

## Requisitos

- Python 3.x
- Conexión en red (interna o localhost) para pruebas.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/"este repo"
   cd PanelC2-Python

Uso
Iniciar el Servidor : Al iniciar el servidor, se abrirá en el puerto 4444(por defecto) y estará listo para aceptar conexiones de clientes.

Interfaz de Operador : El operador verá un menú en la consola con las siguientes opciones:

Mostrar sesiones activas : Muestra un listado de las conexiones activas, cada una con su ID y dirección IP.
Enviar comando a una sesión : Permite al operador enviar un comando específico a una sesión seleccionada por ID.
Salir : Finaliza el programa y cierra el servidor.
Conectar Clientes : Los clientes deben conectarse a la dirección IP del servidor y puerto especificado. Cada cliente conectado se mostrará como una nueva sesión en el listado de sesiones activas.
