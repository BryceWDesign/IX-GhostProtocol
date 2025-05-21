"""
IX-GhostProtocol: utils.py
Provides utility functions for message framing, serialization, and safe parsing.
"""

import json
import struct

def frame_message(data: bytes) -> bytes:
    """
    Prepends message with 4-byte length header.
    """
    return struct.pack(">I", len(data)) + data

def deframe_message(stream: bytes) -> tuple:
    """
    Extracts length-prefixed message from stream.
    Returns (message, remaining_bytes).
    """
    if len(stream) < 4:
        return None, stream
    length = struct.unpack(">I", stream[:4])[0]
    if len(stream) < 4 + length:
        return None, stream
    return stream[4:4+length], stream[4+length:]

def safe_serialize(obj) -> bytes:
    return json.dumps(obj, separators=(",", ":"), sort_keys=True).encode("utf-8")

def safe_deserialize(data: bytes):
    return json.loads(data.decode("utf-8"))
