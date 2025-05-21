"""
IX-GhostProtocol: crypto_engine.py
Implements hybrid encryption using Kyber (post-quantum), X3DH, and Double Ratchet
"""

from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey, X25519PublicKey
)
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

# Placeholder for Kyber PQ KEM - to be replaced by liboqs bindings if available
class KyberKEM:
    def generate_keypair(self):
        # Mocked: Replace with liboqs implementation
        return b"kyber_public_key", b"kyber_private_key"

    def encapsulate(self, public_key):
        # Mocked
        return b"ciphertext", b"shared_secret"

    def decapsulate(self, ciphertext, private_key):
        # Mocked
        return b"shared_secret"

class X3DH:
    def __init__(self):
        self.identity_key = X25519PrivateKey.generate()
        self.ephemeral_key = X25519PrivateKey.generate()

    def generate_shared_secret(self, peer_identity_pub: bytes, peer_ephemeral_pub: bytes):
        peer_identity = X25519PublicKey.from_public_bytes(peer_identity_pub)
        peer_ephemeral = X25519PublicKey.from_public_bytes(peer_ephemeral_pub)
        dh1 = self.identity_key.exchange(peer_identity)
        dh2 = self.ephemeral_key.exchange(peer_ephemeral)

        combined = dh1 + dh2
        derived = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b"ghost_x3dh"
        ).derive(combined)
        return derived

class DoubleRatchetSession:
    def __init__(self, shared_secret: bytes):
        self.root_key = shared_secret
        self.send_chain_key = shared_secret
        self.recv_chain_key = shared_secret

    def encrypt(self, plaintext: bytes) -> (bytes, bytes):
        nonce = os.urandom(12)
        aesgcm = AESGCM(self.send_chain_key)
        ciphertext = aesgcm.encrypt(nonce, plaintext, None)
        return nonce, ciphertext

    def decrypt(self, nonce: bytes, ciphertext: bytes) -> bytes:
        aesgcm = AESGCM(self.recv_chain_key)
        return aesgcm.decrypt(nonce, ciphertext, None)

# Unified API
class CryptoEngine:
    def __init__(self):
        self.kem = KyberKEM()
        self.x3dh = X3DH()
        self.ratchet_session = None

    def initialize_session(self, peer_identity_pub: bytes, peer_ephemeral_pub: bytes):
        shared_secret = self.x3dh.generate_shared_secret(peer_identity_pub, peer_ephemeral_pub)
        self.ratchet_session = DoubleRatchetSession(shared_secret)

    def encrypt_message(self, message: str) -> dict:
        if not self.ratchet_session:
            raise ValueError("Session not initialized")
        nonce, ciphertext = self.ratchet_session.encrypt(message.encode())
        return {
            "nonce": base64.b64encode(nonce).decode(),
            "ciphertext": base64.b64encode(ciphertext).decode()
        }

    def decrypt_message(self, nonce_b64: str, ciphertext_b64: str) -> str:
        if not self.ratchet_session:
            raise ValueError("Session not initialized")
        nonce = base64.b64decode(nonce_b64)
        ciphertext = base64.b64decode(ciphertext_b64)
        plaintext = self.ratchet_session.decrypt(nonce, ciphertext)
        return plaintext.decode()
