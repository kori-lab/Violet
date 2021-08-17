import socket, threading

connections = []

def handle_user_connection(connection: socket.socket, address: str) -> None:
    while True:
        try:
            msg = connection.recv(64)

            if msg:
                print(f'{msg.decode()}')
                
                msg_to_send = f'{msg.decode()}'
                broadcast(msg_to_send, connection)

            else:
                remove_connection(connection)
                break

        except Exception as e:
            print(f'Error to handle user connection: {e}')
            remove_connection(connection)
            break


def broadcast(message: str, connection: socket.socket) -> None:

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

    SERVER_ADDRESS = ''
    LISTENING_PORT = 4444
    
    try:
        socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_instance.bind((SERVER_ADDRESS, LISTENING_PORT))
        socket_instance.listen()

        print(f'Server está ligado!\nEndereço: {socket_instance}')
        
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
