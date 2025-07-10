# Import necessary libraries
import socket
import threading
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Server settings
HOST = '127.0.0.1'
PORT = 55555

# Lists to store clients and usernames
clients = []
usernames = []

# Broadcast message to all connected clients
def broadcast(message, sender_client=None):
    for client in clients:
        if client != sender_client:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                if client in clients:
                    index = clients.index(client)
                    clients.remove(client)
                    usernames.pop(index)

# Handle messages from a single client
def handle_client(client):
    index = clients.index(client)
    username = usernames[index]

    join_message = f"[{datetime.now().strftime('%H:%M:%S')}] {username} has joined the chat."
    print(Fore.YELLOW + join_message)
    broadcast(join_message, client)

    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            timestamp = datetime.now().strftime('%H:%M:%S')
            full_message = f"[{timestamp}] {username}: {message}"
            print(Fore.CYAN + full_message)
            broadcast(full_message, client)
        except:
            client.close()
            clients.remove(client)
            usernames.remove(username)
            leave_message = f"[{datetime.now().strftime('%H:%M:%S')}] {username} has left the chat."
            print(Fore.RED + leave_message)
            broadcast(leave_message)
            break

# Accept new client connections
def receive_connections():
    server.listen()
    print(Fore.RED + f"[SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        client, address = server.accept()
        print(Fore.MAGENTA + f"[NEW CONNECTION] {address}")

        client.send("Enter your username: ".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')

        usernames.append(username)
        clients.append(client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Initialize and run server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

if __name__ == "__main__":
    receive_connections()
