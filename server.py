import socket

class Server:

    def __init__(self, host='127.0.0.1', port=12348):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"Server listening on {self.host}:{self.port}")

    def accept_connection(self):
        client_socket, client_address = self.server_socket.accept()
        print(f"Connection from {client_address}")
        return client_socket

    def receive_data(self, client_socket):
        data = client_socket.recv(1024)
        print(f"Received data: {data.decode('utf-8')}")
        return data.decode('utf-8')

    def close(self):
        self.server_socket.close()

if __name__ == "__main__":
    server = Server()
    client_socket = server.accept_connection()
    server.receive_data(client_socket)
    server.close()
