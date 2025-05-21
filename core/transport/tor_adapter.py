"""
IX-GhostProtocol: tor_adapter.py
Handles communication over Tor hidden services.
Requires Tor to be running locally with ControlPort enabled.
"""

import socket
import socks  # PySocks
import stem
from stem.control import Controller

TOR_SOCKS_PORT = 9050
TOR_CONTROL_PORT = 9051
TOR_PASSWORD = ''  # Optional: set in torrc with HashedControlPassword

class TorAdapter:
    def __init__(self, host="127.0.0.1", port=TOR_SOCKS_PORT):
        self.host = host
        self.port = port
        self.controller = None

    def connect_control_port(self):
        try:
            self.controller = Controller.from_port(port=TOR_CONTROL_PORT)
            self.controller.authenticate(password=TOR_PASSWORD)
        except Exception as e:
            raise RuntimeError(f"Tor control port connection failed: {e}")

    def renew_circuit(self):
        if not self.controller:
            self.connect_control_port()
        self.controller.signal(stem.Signal.NEWNYM)

    def create_socket(self, onion_address, remote_port):
        socks.set_default_proxy(socks.SOCKS5, self.host, self.port)
        s = socks.socksocket()
        try:
            s.connect((onion_address, remote_port))
            return s
        except Exception as e:
            raise RuntimeError(f"Failed to connect to {onion_address}:{remote_port} via Tor: {e}")

    def send_message(self, onion_address, port, message: bytes):
        with self.create_socket(onion_address, port) as s:
            s.sendall(message)
            response = s.recv(4096)
            return response

    def close(self):
        if self.controller:
            self.controller.close()
