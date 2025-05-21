"""
IX-GhostProtocol: storage_engine.py
Provides secure local storage with encryption for sensitive data.
"""

import os
import json
from cryptography.fernet import Fernet

STORAGE_ROOT = "storage/data/"
KEY_FILE = "storage/storage_key.key"

class StorageEngine:
    def __init__(self):
        self.key = self.load_or_create_key()
        self.cipher = Fernet(self.key)
        os.makedirs(STORAGE_ROOT, exist_ok=True)

    def load_or_create_key(self):
        os.makedirs(os.path.dirname(KEY_FILE), exist_ok=True)
        if os.path.exists(KEY_FILE):
            with open(KEY_FILE, "rb") as f:
                return f.read()
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
        return key

    def store_encrypted(self, filename: str, data: dict):
        full_path = os.path.join(STORAGE_ROOT, filename)
        encoded = json.dumps(data).encode()
        encrypted = self.cipher.encrypt(encoded)
        with open(full_path, "wb") as f:
            f.write(encrypted)

    def load_encrypted(self, filename: str) -> dict:
        full_path = os.path.join(STORAGE_ROOT, filename)
        if not os.path.exists(full_path):
            return {}
        with open(full_path, "rb") as f:
            encrypted = f.read()
        decrypted = self.cipher.decrypt(encrypted)
        return json.loads(decrypted.decode())
