import socket
import random
import time

class Client:
    def __init__(self, host='127.0.0.1', port=12348):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to server at {self.host}:{self.port}")

    def send_data(self, data):
        self.client_socket.sendall(data.encode('utf-8'))
        print(f"Sent data: {data}")

    def close(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = Client()
    client.connect_to_server()
    data = str(random.randint(1, 100))  # Generate random data
    client.send_data(data)
    client.close()
