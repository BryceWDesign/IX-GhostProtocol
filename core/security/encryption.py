"""
IX-GhostProtocol: encryption.py
Provides AES-GCM encryption and decryption for secure message confidentiality.
"""

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class EncryptionManager:
    def __init__(self, key: bytes = None):
        self.key = key or AESGCM.generate_key(bit_length=256)
        self.aesgcm = AESGCM(self.key)

    def encrypt(self, plaintext: bytes, associated_data: bytes = None) -> tuple:
        nonce = os.urandom(12)
        ciphertext = self.aesgcm.encrypt(nonce, plaintext, associated_data)
        return nonce, ciphertext

    def decrypt(self, nonce: bytes, ciphertext: bytes, associated_data: bytes = None) -> bytes:
        return self.aesgcm.decrypt(nonce, ciphertext, associated_data)

    def export_key(self) -> bytes:
        return self.key
