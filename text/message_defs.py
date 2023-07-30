from pydantic import BaseModel, StrictStr
from dataclasses import dataclass
from enum import Enum

class RoleOptions(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

class Message(BaseModel):
    role: str
    content: str

class MessageType(str, Enum):
    MESSAGE = "message"
    HISTORY_MESSAGE = "history_message"
    PRIMER_MESSAGE = "primer_message"
    PROMPT_MESSAGE = "prompt_message"
    PROMPT_CHAIN_MESSAGE = "chain_message"
    PERSONA_MESSAGE = "persona_message"

class StoredMessage(BaseModel):
    message: Message
    message_type: MessageType

    class Config:
        population_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            MessageType: lambda v: v.value,
        }

class HistoryMessage(StoredMessage):
    message_type: MessageType = MessageType.HISTORY_MESSAGE

class PrimerMessage(StoredMessage):
    message_type: MessageType = MessageType.PRIMER_MESSAGE
    message_title: StrictStr

class PromptMessage(StoredMessage):
    message_type: MessageType = MessageType.PROMPT_MESSAGE
    message_title: StrictStr

class PromptChainMessage(StoredMessage):
    message_type: MessageType = MessageType.PROMPT_CHAIN_MESSAGE
    message_title: StrictStr
    message_description: StrictStr

class PersonaMessage(StoredMessage):
    message_type: MessageType = MessageType.PERSONA_MESSAGE