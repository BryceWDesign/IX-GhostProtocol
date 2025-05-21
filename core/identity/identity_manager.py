"""
IX-GhostProtocol: identity_manager.py
Manages local identity key generation, loading, and storage.
"""

import os
import json
from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey, X25519PublicKey
)
from cryptography.hazmat.primitives import serialization

IDENTITY_FILE = "storage/identity.json"

class IdentityManager:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.load_or_generate_keys()

    def load_or_generate_keys(self):
        if os.path.exists(IDENTITY_FILE):
            with open(IDENTITY_FILE, "r") as f:
                data = json.load(f)
                priv_bytes = bytes.fromhex(data["private_key"])
                self.private_key = X25519PrivateKey.from_private_bytes(priv_bytes)
                self.public_key = self.private_key.public_key()
        else:
            self.private_key = X25519PrivateKey.generate()
            self.public_key = self.private_key.public_key()
            self.save_keys()

    def save_keys(self):
        priv_bytes = self.private_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption()
        )
        data = {
            "private_key": priv_bytes.hex()
        }
        os.makedirs(os.path.dirname(IDENTITY_FILE), exist_ok=True)
        with open(IDENTITY_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def get_private_key_bytes(self):
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption()
        )

    def get_public_key_bytes(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
