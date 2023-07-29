from text.message_defs import (
    Message, 
    RoleOptions
)
import json
from json.encoder import JSONEncoder


encoder = JSONEncoder(sort_keys=True,ensure_ascii=True)

class Messages:
    def __init__(self):
        pass
    
    def create_message(self, role: RoleOptions, content: str) -> Message:
        return Message(role=role, content=content)

    def prompt_message_to_json(self, prompts: list) -> str:
        return json.dumps(prompts)

    def json_to_prompt_message(self, json_str: str) -> list:
        return json.loads(json_str)

    def prompt_chain_message_to_json(self, chains: list) -> str:
        return json.dumps(chains)

    def json_to_prompt_chain_message(self, json_str: str) -> list:
        return json.loads(json_str)

    def primer_message_to_json(self, primers: list) -> str:
        return json.dumps(primers)

    def json_to_primer_message(self, json_str: str) -> list:
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

    def message_to_json(self, message: dict) -> str:
        return json.dumps(message)

    def json_to_message(self, json_str: str) -> dict:
        return json.loads(json_str)