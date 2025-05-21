# IX-GhostProtocol: Technical Specification & Threat Model

## Overview
IX-GhostProtocol is a censorship-proof, metadata-resistant communication system that eliminates surveillance risk through obfuscated routing, anonymous key exchange, and zero-identifier transport. It is fully peer-to-peer, post-quantum ready, and platform-independent.

---

## Core Design Goals

1. **Zero Metadata:** No IPs, MACs, timestamps, UUIDs, or routing IDs.
2. **Quantum-Resistant Encryption:** Hybrid post-quantum + forward-secrecy.
3. **Untraceable Routing:** Multi-hop onion routing + cover traffic.
4. **No Accounts, No Identities:** All keys are ephemeral or renewable without central storage.
5. **Modular Transport:** Tor hidden services, Mixnets, I2P fallback.

---

## Threat Model

| Threat | Defense |
|--------|---------|
| Passive surveillance (ISP, nation-states) | Onion routing, traffic shaping, no identifiers |
| Metadata collection (contact graphs, IP logs) | Ephemeral keys, constant packet sizes, no central servers |
| Active probing (packet injection or traffic fingerprinting) | Cover traffic, pluggable transports |
| Cryptanalysis (future quantum attackers) | Kyber (Lattice-based) + X3DH hybrid protocol |
| Server compromise | No servers used (pure P2P), relays are blinded |
| User compromise | Ephemeral identity, message deniability |

---

## Protocol Stack

1. **Application Layer**
   - Constant-sized encrypted blobs
   - Optional CLI or GUI interface
2. **Encryption Layer**
   - X3DH + Double Ratchet + Kyber encapsulation
3. **Transport Layer**
   - Tor v3 Onion Services by default
   - I2P, Loopix-style Mixnet fallbacks
4. **Routing Layer**
   - Multi-hop randomized path with noise generation
5. **Identity Layer**
   - Public key-based addressing, no usernames
   - Key rotation by default

---

## Default Packet Structure (Fixed-size)

```
| Header (32 bytes) | Payload (512 bytes) | Padding (variable) |
```

- All messages are padded to 1024 bytes to resist packet size analysis.

---

## Future Plans

- Decoy node simulation
- Steganographic transport channels
- Bridge relay deployment via WebRTC/IPFS hybrid transport

---

## References & Inspirations

- Signal Protocol (Open Whisper Systems)
- Cwtch (Ricochet successor)
- SimpleX Messaging
- Loopix Mixnet
- Nym SDK
- liboqs / Kyber
