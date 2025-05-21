# core/utils/__init__.py
# Initializes the utils module for IX-GhostProtocol

from .utils import (
    frame_message,
    deframe_message,
    safe_serialize,
    safe_deserialize
)

__all__ = [
    "frame_message",
    "deframe_message",
    "safe_serialize",
    "safe_deserialize"
]
