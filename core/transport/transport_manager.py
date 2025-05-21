"""
IX-GhostProtocol: transport_manager.py
Handles low-level transport of encrypted messages over TCP sockets.
"""

import socket
import threading
from typing import Callable, Optional

class TransportManager:
    def __init__(self, host: str, port: int, on_message: Optional[Callable] = None):
        self.host = host
        self.port = port
        self.on_message = on_message
        self.server_socket = None
        self.client_sockets = []
        self.running = False

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.running = True
        threading.Thread(target=self.accept_clients, daemon=True).start()

    def accept_clients(self):
        while self.running:
            client_sock, addr = self.server_socket.accept()
            self.client_sockets.append(client_sock)
            threading.Thread(target=self.handle_client, args=(client_sock,), daemon=True).start()

    def handle_client(self, client_sock: socket.socket):
        try:
            while True:
                data = client_sock.recv(4096)
                if not data:
                    break
                if self.on_message:
                    self.on_message(data, client_sock)
        finally:
            client_sock.close()
            if client_sock in self.client_sockets:
                self.client_sockets.remove(client_sock)

    def send_message(self, client_sock: socket.socket, message: bytes):
        client_sock.sendall(message)

    def broadcast_message(self, message: bytes):
        for sock in self.client_sockets:
            self.send_message(sock, message)

    def stop_server(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        for sock in self.client_sockets:
            sock.close()
        self.client_sockets.clear()
