# IX-GhostProtocol – Steganography Specification

This document outlines the steganographic techniques supported by IX-GhostProtocol to hide encrypted payloads within benign media, enhancing metadata resistance and stealth.

---

## 🖼 Supported Media Types

- Images (PNG, BMP) using least significant bit (LSB) embedding.
- Audio (WAV) via phase coding and echo hiding.
- Text (whitespace, zero-width characters).

---

## 🔍 Embedding Techniques

- **LSB Embedding (Images):**  
  Embed encrypted bytes in least significant bits of pixel color channels.  
  Use random pixel selection seeded by shared secret to avoid patterns.

- **Phase Coding (Audio):**  
  Modulate phase components of audio signal to encode data without perceptible change.

- **Whitespace/Text:**  
  Insert zero-width spaces or Unicode invisibles at pseudo-random intervals.

---

## 📡 Transmission

- Stego media files sent over common platforms (email, social media, file sharing).
- No metadata leakage from the carrier media since it appears unaltered to casual inspection.

---

## 🔑 Key Integration

- Embedding locations and patterns are derived from shared session keys.
- Carrier files can be reused or generated dynamically.

---

## 🔄 Extraction

- Receiver uses shared secret to locate embedded payload bits.
- Extracted payload is decrypted via AES-GCM session key.

---

## ⚠️ Limitations

- Stego channels reduce effective bandwidth significantly.
- Robustness against active attackers depends on carrier media choice and transmission method.

---

## 🛠 Extensibility

- Modular plugin system to add new stego techniques.
- Support for video and network steganography planned for future versions.
