import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen()

clients = []

def accept_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        print(f"Connection from {client_address}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Received message: {message}")
                broadcast(message, client_socket)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                clients.remove(client)

def start_server():
    server_thread = threading.Thread(target=accept_connections)
    server_thread.daemon = True
    server_thread.start()

if __name__ == "__main__":
    print("Server is running...")
    start_server()
    while True:
        pass
