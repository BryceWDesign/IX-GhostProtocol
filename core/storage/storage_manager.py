"""
IX-GhostProtocol: storage_manager.py
Handles encrypted persistent storage of protocol metadata and peer state.
"""

import os
import json
from cryptography.fernet import Fernet


class StorageManager:
    def __init__(self, storage_file: str = "ghost_store.json.enc", key_file: str = "ghost_store.key"):
        self.storage_file = storage_file
        self.key_file = key_file
        self.key = self._load_or_generate_key()
        self.fernet = Fernet(self.key)
        self.data = self._load_storage()

    def _load_or_generate_key(self) -> bytes:
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                return f.read()
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as f:
            f.write(key)
        return key

    def _load_storage(self) -> dict:
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "rb") as f:
                decrypted = self.fernet.decrypt(f.read())
                return json.loads(decrypted.decode("utf-8"))
        return {}

    def save(self):
        with open(self.storage_file, "wb") as f:
            encrypted = self.fernet.encrypt(json.dumps(self.data).encode("utf-8"))
            f.write(encrypted)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save()
