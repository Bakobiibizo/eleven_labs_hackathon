import json
from pydantic import BaseModel
from typing import Optional

class Voice(BaseModel):
    name: str
    voice_id: str
    age: str
    gender: str
    accent: Optional[str] = None
    description: Optional[str] = None
    use_case: Optional[str] = None

class Voices:
    def __init__(self):
        self.voices = []
        
    def add(self, voice: Voice):
        with open("voice/voices.json", "r") as f:
            json_string = f.read()
        self.voices.append(voice.model_dump())
        self.voices = json_string
        with open("voice/voice_choices.json", "a") as f:
            f.write(json.dumps(self.voices))
        
    def get(self):
        return self.voices

