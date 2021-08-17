import socket, threading

connections = []

def handle_user_connection(connection: socket.socket, address: str) -> None:
    while True:
        try:
            msg = connection.recv(1024).decode()

            if msg:
                print(f'\n{msg}')
                
                msg_to_send = f'{msg}'
                broadcast(msg_to_send, connection)

            else:
                remove_connection(connection)
                break

        except Exception as e:
            print(f'Erro ao lidar com a conexão do usuário: {e}')
            remove_connection(connection)
            break


def broadcast(message: str, connection: socket.socket) -> None:
    if not message:
        pass;
    for client_conn in connections:
        if client_conn != connection:
            try:
                client_conn.send(message.encode())

            except Exception as e:
                print('Error broadcasting message: {e}')
                remove_connection(client_conn)


def remove_connection(conn: socket.socket) -> None:
    if conn in connections:
        conn.close()
        connections.remove(conn)


def server() -> None:

    LISTENING_PORT = 5000
    
    try:
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind(('', LISTENING_PORT))
        socket_instance.listen()

        print(f'Server está ligado!\nEndereço ip: {socket.gethostbyname(socket.gethostname())}')
        
        while True:
            socket_connection, address = socket_instance.accept()
            connections.append(socket_connection)

            threading.Thread(target=handle_user_connection, args=[socket_connection, address]).start()

    except Exception as e:
        print(f'Ocorreu um erro ao instanciar socket: {e}')
    finally:

        if len(connections) > 0:
            for conn in connections:
                remove_connection(conn)

        socket_instance.close()
