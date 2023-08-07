from text.message_defs import Message
from text.context_window import ContextWindow
import json
from json.encoder import JSONEncoder



encoder = JSONEncoder(sort_keys=True,ensure_ascii=True)


class Messages:
    def __init__(self):
        self.context_window = ContextWindow(window_size=50)
        self.context = self.context_window.get_context()
        self.start_context()
    
    def create_message(self, role: str, content: str, model: str) -> Message:
        Message(role=role, content=content)
        self.context_window.add_message(message=Message(role=role, content=content, model=model))
        messages = self.context_window.get_context()
        return messages     
    
    def start_context(self):
        self.context_window.start_context()
           

    def prompt_chain_message_to_json(self, chains: list) -> str:
        return json.dumps(chains)

    def json_to_prompt_chain_message(self, json_str: str) -> list:
        return json.loads(json_str)

    def persona_message_to_json(self, personas: list) -> str:
        return json.dumps(personas)

    def json_to_persona_message(self, json_str: str) -> list:
        return json.loads(json_str)

    def history_message_to_json(self, message_history: list) -> str:
        for message in message_history:
            try:
                iterable = iter(message)
            except TypeError:
                pass
            else: 
                return list(iterable)

    def json_to_history_message(self, json_str: str) -> list:
        return json.loads(json_str)

    def message_to_json(self, message: Message) -> str:
        return json.dumps(message.dict())

    def json_to_message(self, json_str: str) -> dict:
        return json.loads(json_str)