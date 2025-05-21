# IX-GhostProtocol – Architecture Overview

IX-GhostProtocol is a decentralized, metadata-resistant communication framework designed to operate under hostile network conditions, censorship, and surveillance. It combines principles from mesh networking, onion routing, steganographic signaling, and public-key authentication to create a robust ghost-layer communications protocol.

---

## 📐 System Layers

**1. Application Layer (`apps/`)**
- Command-line interface (CLI) and service APIs for user interaction.

**2. Protocol Core (`core/`)**
- Handles routing, encryption, session management, transport, and wire formats.

**3. Storage Layer (`core/storage/`)**
- Metadata-free file-based memory and optional steganographic persistence.

**4. Wire Layer (`core/wire/`)**
- Defines the structure, encoding, and decoding of low-level data packets.

---

## 🔐 Security Model

- End-to-end encryption using AES-GCM with ephemeral keys.
- Optional out-of-band key exchange with QR code or USB sneakernet.
- Resilient to metadata leakage by storing no headers, MAC addresses, or timestamps.

---

## 🔀 Routing Topology

- Stateless hop-by-hop routing.
- Pluggable routing algorithms: random relay, time-delay mesh, or proof-of-forwarding.
- Optional Tor/I2P-style overlays or peer-to-peer wormhole tunnels.

---

## 📁 Storage and State

- No user tracking, no identity beaconing.
- Flat-file encrypted session data with integrity checks.
- Stateless session mode and optional "ghost state" recovery.

---

## 📡 Transport Layer

- Default: UDP with AES-GCM payloads.
- Experimental: DNS tunneling, covert HTTP GETs, ICMP pingback chains.

---

## 🛠 Extensibility

- Modular core services and replaceable layers.
- Plugin-ready architecture for routing, encryption, steganography, transport.

---

## 🧭 Governance

- Open-source and free for civilian and emergency use.
- Licensed under the Affero General Public License (AGPL) v3 to ensure that all modifications and network-based uses remain open-source and contribute back to the community.
- This license choice promotes transparency, collaboration, and ensures IX remains free and open in all deployments.
