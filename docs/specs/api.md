# IX-GhostProtocol – API Specification

This document describes the external interfaces exposed by IX-GhostProtocol for applications to interact with the protocol securely and efficiently.

---

## 🎯 API Goals

- Provide simple, secure methods for messaging and network management.
- Abstract complex cryptographic and routing details.
- Support asynchronous and event-driven usage.
- Enable extensibility and cross-language bindings.

---

## 📨 Messaging API

### send_message(destination: PublicKey, message: bytes) -> MessageID
- Encrypts and routes the message to the specified destination.
- Returns a unique message ID for tracking.

### receive_message() -> (MessageID, PublicKey, bytes)
- Retrieves the next decrypted message available.
- Includes sender’s public key for authentication.

### delete_message(message_id: MessageID) -> bool
- Securely deletes the specified message from local storage.

---

## 🌐 Network API

### connect_peer(peer_address: str) -> bool
- Establishes a connection to a peer node.

### disconnect_peer(peer_id: PublicKey) -> bool
- Terminates connection to specified peer.

### get_peer_list() -> List[PublicKey]
- Returns current connected peers.

### discover_peers() -> List[PublicKey]
- Initiates peer discovery process.

---

## 🔐 Key Management API

### generate_keypair() -> (PublicKey, PrivateKey)
- Creates a new cryptographic key pair.

### import_key(private_key: bytes) -> bool
- Imports an existing private key.

### export_public_key() -> PublicKey
- Returns the current public key.

---

## 🧩 Event Hooks

- on_message_received(callback)
- on_peer_connected(callback)
- on_peer_disconnected(callback)
- on_error(callback)

---

## Security Considerations

- All API calls must be authenticated where applicable.
- Sensitive data never exposed in plaintext via API.
- Rate limiting and access control mechanisms.

---

## Extensibility

- Supports bindings for Python, Rust, Go, and JavaScript planned.
- API versioning for backward compatibility.

