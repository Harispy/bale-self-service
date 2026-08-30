from enum import Enum

class ChatType(int, Enum):
    """
    Enum representing different types of chat.
    """
    
    UNKNOWN = 0
    """Represents an unknown chat type."""

    PRIVATE = 1
    """Represents a private chat."""

    GROUP = 2
    """Represents a group chat."""

    CHANNEL = 3
    """Represents a channel chat."""

    BOT = 4
    """Represents a bot chat."""

    SUPER_GROUP = 5
    THREAD = 6
    """Represents a super group chat."""
