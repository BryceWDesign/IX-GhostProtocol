# core/transport/__init__.py
# Initializes the transport module for IX-GhostProtocol

from .tor_adapter import TorAdapter

__all__ = ["TorAdapter"]
