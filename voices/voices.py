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
    def __init__(self, name=None, voice_id=None, accent=None, description=None, age=None, gender=None, use_case=None):
        self.voices = []
        self.name = name
        self.voice_id = voice_id
        self.accent = accent
        self.description = description
        self.age = age
        self.gender = gender
        self.use_case = use_case
        
    def add(self, voice: Voice):
        with open("voices/voices.json", "r") as f:
            json_string = f.read()
        self.voices.append(voice.model_dump())
        self.voices = json_string
        with open("voices/voice_choices.json", "a") as f:
            f.write(json.dumps(self.voices))
        
    def get(self):
        return self.voices

#    def make_tools(self):
#        voice_data_array = []
#        with open ("voice_choices.json", "r") as f:
#            json_string = f.read()
#        voice_data_array.append(json.loads(json_string))
#        for voice in voice_data_array:
            
    
       