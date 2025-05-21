"""
IX-GhostProtocol: transport_layer.py
Implements UDP-based encrypted transport layer for decentralized communication.
"""

import socket
import threading
from core.security import EncryptionManager


class TransportLayer:
    def __init__(self, host: str = "0.0.0.0", port: int = 9999, encryption_key: bytes = None):
        self.host = host
        self.port = port
        self.encryption = EncryptionManager(encryption_key)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.running = False
        self.handlers = []

    def start(self):
        self.sock.bind((self.host, self.port))
        self.running = True
        threading.Thread(target=self._receive_loop, daemon=True).start()

    def _receive_loop(self):
        while self.running:
            try:
                data, addr = self.sock.recvfrom(65535)
                nonce = data[:12]
                ciphertext = data[12:]
                decrypted = self.encryption.decrypt(nonce, ciphertext)
                for handler in self.handlers:
                    handler(decrypted, addr)
            except Exception:
                continue

    def send(self, data: bytes, target: tuple):
        nonce, ciphertext = self.encryption.encrypt(data)
        self.sock.sendto(nonce + ciphertext, target)

    def register_handler(self, handler):
        self.handlers.append(handler)

    def stop(self):
        self.running = False
        self.sock.close()
