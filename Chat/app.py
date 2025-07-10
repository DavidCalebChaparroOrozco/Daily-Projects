# Import necessary libraries
import socket
import threading
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Server connection settings
HOST = '127.0.0.1'
PORT = 55555

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Get and send username
username = input("Choose your username: ")
client.send(username.encode('utf-8'))

# Function to receive messages from server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if username in message:
                print(Fore.GREEN + message)  # Your own messages
            elif "has joined" in message or "has left" in message:
                print(Fore.YELLOW + message)  # Join/leave messages
            else:
                print(Fore.CYAN + message)  # Messages from others
        except:
            print(Fore.RED + "Disconnected from server.")
            client.close()
            break

# Function to send messages to server
def send_messages():
    while True:
        message = input()
        client.send(message.encode('utf-8'))

# Start threads for sending and receiving
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
