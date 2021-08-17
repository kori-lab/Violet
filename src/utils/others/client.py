import socket, threading
from src.utils.functions.randomColor import *
from src.utils.functions.selfInput import *
from src.utils.functions.clear import *

def handle_messages(connection: socket.socket):
    while True:
        try:
            msg = connection.recv(64)

            if msg:
                print("\n"+ msg.decode())
            else:
                connection.close()
                break

        except Exception as e:
            print(f'Alguém saiu...')
            connection.close()
            break

def client() -> None:
    # localhost
    SERVER_ADDRESS = selfInput('\nQual é o endereço do servidor?')
    SERVER_PORT = 4545

    try:
        socket_instance = socket.socket()
        socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
        threading.Thread(target=handle_messages, args=[socket_instance]).start()

        name = selfInput('\nQual é seu nome?').capitalize()

        clear();
        print('\nConectado no chat! digite sair para sair do chat...')
        
        name = f'{randomColor(name)}\033[0;0m'

        while True:
            msg = input('')

            if msg == 'sair':
                break

            msg = f"{name} - {msg}"
            socket_instance.send(msg.encode())

        socket_instance.close()

    except Exception as e:
        print(f'Erro ao se conectar no servidor: {e}')
        socket_instance.close()

