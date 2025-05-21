# IX-GhostProtocol – Cryptographic Specification

This document defines the cryptographic primitives and key management techniques used by IX-GhostProtocol to provide metadata-resilient, forward-secure communication.

---

## 🔐 Core Cryptographic Goals

- **Confidentiality**: All payloads are encrypted end-to-end using ephemeral session keys.
- **Integrity**: Messages are authenticated using Galois/Counter Mode (GCM).
- **Plausible Deniability**: Key rotation and ghost sessions allow perfect forward secrecy.
- **Metadata Resistance**: Encrypted blobs include no MAC addresses, timestamps, IPs, or routing data.

---

## 🔑 Key Management

### Long-Term Keys
- Stored locally, never transmitted.
- Generated with `cryptography.hazmat.primitives.asymmetric.ed25519`.

### Ephemeral Session Keys
- Per-session AES-256-GCM key derived via X25519 key exchange.
- Keys are destroyed after session ends unless ghost recovery is enabled.

---

## 🔁 Key Exchange Protocol

1. Generate ephemeral X25519 private/public key pair.
2. Exchange public keys through stego-channel or sneakernet (QR, USB, covert channel).
3. Derive shared secret via ECDH:
   ```
   shared_secret = X25519(priv_local, pub_remote)
   session_key = HKDF(shared_secret)
   ```
4. Encrypt packets using AES-256-GCM with session key.

---

## 🔒 Encryption / Decryption

```python
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Encrypt
aesgcm = AESGCM(session_key)
ciphertext = aesgcm.encrypt(nonce, data, aad=None)

# Decrypt
plaintext = aesgcm.decrypt(nonce, ciphertext, aad=None)
```

---

## 🧪 Hashing and Integrity

- SHA256 for internal key ID hashing.
- HMAC-SHA256 for internal routing validation (optional).
- Nonces must be 12 bytes and randomly generated per message.

---

## 🧼 Key Hygiene

- Ephemeral keys wiped from memory after use.
- No session IDs or headers exposed in any transmission.
- Recovery keys optionally stored offline in steganographic media.
