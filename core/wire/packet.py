"""
IX-GhostProtocol: packet.py
Defines wire-level packet structure and serialization/deserialization logic.
"""

import struct
import json


class GhostPacket:
    def __init__(self, msg_type: str, payload: dict):
        self.msg_type = msg_type
        self.payload = payload

    def serialize(self) -> bytes:
        """Serialize message type and JSON-encoded payload to bytes."""
        msg_type_bytes = self.msg_type.encode("utf-8")
        payload_bytes = json.dumps(self.payload).encode("utf-8")
        header = struct.pack("!H", len(msg_type_bytes))
        return header + msg_type_bytes + payload_bytes

    @staticmethod
    def deserialize(data: bytes):
        """Deserialize bytes back into a GhostPacket."""
        if len(data) < 2:
            raise ValueError("Invalid packet data")
        msg_type_len = struct.unpack("!H", data[:2])[0]
        msg_type = data[2:2+msg_type_len].decode("utf-8")
        payload = json.loads(data[2+msg_type_len:].decode("utf-8"))
        return GhostPacket(msg_type, payload)
