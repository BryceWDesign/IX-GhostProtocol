"""
IX-GhostProtocol: routing_manager.py
Handles basic message routing and loop prevention across peers.
"""

import hashlib
import time
from typing import Dict, Set

class RoutingManager:
    def __init__(self):
        self.seen_messages: Set[str] = set()
        self.route_table: Dict[str, str] = {}  # destination_id -> next_hop_id
        self.expiry_time_sec = 300  # Optional: clear old entries

    def has_seen(self, message_id: str) -> bool:
        return message_id in self.seen_messages

    def mark_seen(self, message_id: str):
        self.seen_messages.add(message_id)

    def generate_message_id(self, payload: bytes) -> str:
        return hashlib.sha256(payload).hexdigest()

    def add_route(self, destination_id: str, next_hop_id: str):
        self.route_table[destination_id] = next_hop_id

    def get_next_hop(self, destination_id: str) -> str:
        return self.route_table.get(destination_id, None)

    def clear_old_routes(self):
        # Optional future: add TTLs for routes
        pass
