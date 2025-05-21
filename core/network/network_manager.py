"""
IX-GhostProtocol: network_manager.py
Manages peer discovery, connections, and message routing.
"""

import threading
import time
import random
from typing import Dict, List, Optional
from core.identity.identity_manager import IdentityManager

class NetworkManager:
    def __init__(self, identity: IdentityManager):
        self.identity = identity
        self.peers: Dict[str, dict] = {}  # peer_id -> metadata
        self.lock = threading.Lock()

    def add_peer(self, peer_id: str, metadata: dict):
        with self.lock:
            self.peers[peer_id] = metadata

    def remove_peer(self, peer_id: str):
        with self.lock:
            if peer_id in self.peers:
                del self.peers[peer_id]

    def get_peers(self) -> List[str]:
        with self.lock:
            return list(self.peers.keys())

    def broadcast_message(self, message: bytes):
        # Placeholder: iterate over peers and send message using transport
        for peer_id in self.get_peers():
            # Implement transport send here
            pass

    def discover_peers(self):
        # Placeholder: implement peer discovery mechanism (e.g., DHT or bootstrap)
        # This method should run in a background thread or be called periodically
        pass

    def start_peer_discovery(self, interval_sec=60):
        def discovery_loop():
            while True:
                self.discover_peers()
                time.sleep(interval_sec)
        t = threading.Thread(target=discovery_loop, daemon=True)
        t.start()
