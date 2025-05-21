"""
IX-GhostProtocol: crypto_utils.py
Provides helper functions for cryptographic operations such as key encoding and hashing.
"""

import base64
import hashlib


def encode_key(key: bytes) -> str:
    """Encodes binary key to Base64 string for storage or transport."""
    return base64.urlsafe_b64encode(key).decode("utf-8")


def decode_key(encoded_key: str) -> bytes:
    """Decodes Base64 string back to binary key."""
    return base64.urlsafe_b64decode(encoded_key.encode("utf-8"))


def sha256(data: bytes) -> str:
    """Returns hex-encoded SHA256 digest of input bytes."""
    return hashlib.sha256(data).hexdigest()
