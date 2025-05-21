# IX-GhostProtocol – Command Line Interface (CLI) Specification

This document defines the CLI commands and options available to users for controlling IX-GhostProtocol instances.

---

## 🎯 CLI Goals

- Provide secure, user-friendly control over the protocol.
- Enable automation and scripting.
- Support interactive and non-interactive modes.

---

## 🖥 CLI Commands

### Initialization & Configuration

- `ixgp init [--config <file>]`
  - Initialize protocol with optional config file.

- `ixgp config set <key> <value>`
  - Set configuration parameter.

- `ixgp config get <key>`
  - Retrieve configuration parameter.

---

### Key Management

- `ixgp key generate`
  - Generate new ephemeral keys.

- `ixgp key import <file>`
  - Import keys from file.

- `ixgp key export <file>`
  - Export keys securely.

---

### Messaging

- `ixgp send --to <destination> --message <text> [--options]`
  - Encrypt and send a message.

- `ixgp receive [--wait]`
  - Receive messages; waits if specified.

- `ixgp delete --id <messageId>`
  - Securely delete a message.

---

### Session Control

- `ixgp session start --peer <peerId>`
  - Start secure session.

- `ixgp session end --peer <peerId>`
  - End session.

---

### Diagnostics

- `ixgp status`
  - Display current protocol status.

- `ixgp logs [--level <severity>]`
  - Show logs filtered by severity.

---

## 🔧 CLI Options

- `--verbose` / `-v` : Increase output verbosity.
- `--help` / `-h` : Show help for commands.
- `--quiet` / `-q` : Suppress output except errors.

---

## Security Considerations

- CLI commands never print sensitive keys or raw plaintext.
- Authentication enforced for sensitive operations.

---

## Extensibility

- Plugin commands can be added dynamically.
- Scriptable interface supports automation tools.

