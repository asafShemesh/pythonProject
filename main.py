import threading
import random
import time  # Import time module
from server import Server
from client import Client

def run_server():
    server = Server()
    client_socket = server.accept_connection()
    server.receive_data(client_socket)
    server.close()

def run_client():
    client = Client()
    client.connect_to_server()
    data = str(random.randint(1000, 2000))  # Generate random data
    client.send_data(data)
    client.close()

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    client_thread = threading.Thread(target=run_client)

    server_thread.start()
    # Sleep for a bit to ensure server starts listening before client connects
    time.sleep(1)
    client_thread.start()

    server_thread.join()
    client_thread.join()
