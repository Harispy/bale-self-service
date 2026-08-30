from pydantic import Field
from typing import TYPE_CHECKING, Optional

from ..enums import ChatType
from .base import BaleObject

class Chat(BaleObject):
    """
    Represents a chat object in the Bale system.

    Attributes:
        type (ChatType): The type of the chat (e.g., private, group, etc.).
        id (int): The unique identifier for the chat.
    """
    
    type: ChatType = Field(..., alias="1")
    """The type of the chat. This field is required and uses an alias '1' for serialization."""

    id: int = Field(..., alias="2")
    """The unique identifier for the chat. This field is required and uses an alias '2' for serialization."""

    access_hash: Optional[int] = Field(None, alias="3")
    """Optional access hash."""

    if TYPE_CHECKING:
        # This init is only used for type checking and IDE autocomplete.
        # It will not be included in runtime behavior.
        def __init__(
            __pydantic__self__,
            *,
            type: ChatType,
            id: int,
            access_hash: Optional[int] = None,
            **__pydantic_kwargs
        ) -> None:
            super().__init__(type=type, id=id, access_hash=access_hash, **__pydantic_kwargs)
