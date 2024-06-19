import socket
import threading

client_socket = None

def start_client():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected to server")
    threading.Thread(target=receive_messages).start()

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Message received: {message}")
                on_message_received(message)
        except:
            break

def on_message_received(message):
    pass  # This function will be overridden in main.py

def send_message(message):
    if client_socket:
        client_socket.send(message.encode())