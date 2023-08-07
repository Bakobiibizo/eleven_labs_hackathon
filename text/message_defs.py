from pydantic import BaseModel
from enum import Enum



class Message(BaseModel):
    role: str
    content: str

class MessageType(str, Enum):
    MESSAGE = "message"
    HISTORY_MESSAGE = "history_message"
    PRIMER_MESSAGE = "primer_message"
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
    stored_message: StoredMessage

class PromptChainMessage(HistoryMessage):
    history_message: HistoryMessage
    message_title: str
    message_description: str

class PersonaMessage(StoredMessage):
    prompt_chain_message: PromptChainMessage
    persona_avatar: str
    