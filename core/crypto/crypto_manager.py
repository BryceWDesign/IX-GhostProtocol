"""
IX-GhostProtocol: crypto_manager.py
Provides cryptographic primitives for encryption, decryption, and key exchange.
"""

from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey, X25519PublicKey
)
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

class CryptoManager:
    def __init__(self, private_key: X25519PrivateKey):
        self.private_key = private_key

    def generate_shared_key(self, peer_public_bytes: bytes) -> bytes:
        peer_public_key = X25519PublicKey.from_public_bytes(peer_public_bytes)
        shared_key = self.private_key.exchange(peer_public_key)
        # Derive AES key by truncation or KDF (simplified here)
        return shared_key[:32]

    def encrypt(self, key: bytes, plaintext: bytes, associated_data: bytes = b"") -> bytes:
        nonce = os.urandom(12)
        aesgcm = AESGCM(key)
        ct = aesgcm.encrypt(nonce, plaintext, associated_data)
        return nonce + ct

    def decrypt(self, key: bytes, ciphertext: bytes, associated_data: bytes = b"") -> bytes:
        nonce = ciphertext[:12]
        ct = ciphertext[12:]
        aesgcm = AESGCM(key)
        return aesgcm.decrypt(nonce, ct, associated_data)
