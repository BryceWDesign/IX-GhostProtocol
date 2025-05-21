"""
IX-GhostProtocol: identity_manager.py
Manages cryptographic identity, keypair generation, and persistent fingerprints.
"""

import os
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


class IdentityManager:
    def __init__(self, key_path: str = "node.key"):
        self.key_path = key_path
        self.private_key = None
        self.public_key = None
        self.node_id = None
        self._load_or_generate_keys()

    def _load_or_generate_keys(self):
        if os.path.exists(self.key_path):
            with open(self.key_path, "rb") as f:
                self.private_key = serialization.load_pem_private_key(
                    f.read(),
                    password=None,
                    backend=default_backend()
                )
        else:
            self.private_key = ed25519.Ed25519PrivateKey.generate()
            with open(self.key_path, "wb") as f:
                f.write(
                    self.private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.PKCS8,
                        encryption_algorithm=serialization.NoEncryption()
                    )
                )

        self.public_key = self.private_key.public_key()
        self.node_id = self.get_fingerprint()

    def get_fingerprint(self) -> str:
        pub_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        return pub_bytes.hex()

    def sign(self, data: bytes) -> bytes:
        return self.private_key.sign(data)

    def verify(self, signature: bytes, data: bytes, public_key_bytes: bytes) -> bool:
        try:
            pub_key = ed25519.Ed25519PublicKey.from_public_bytes(public_key_bytes)
            pub_key.verify(signature, data)
            return True
        except Exception:
            return False

    def get_public_key_bytes(self) -> bytes:
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
