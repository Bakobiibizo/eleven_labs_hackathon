from text.openai_text import OpenAITextGeneration
from text.create_messages import Messages
from voice.eleven_labs import TextToSpeach
from image.generate_image import GenerateImage
from fastapi import HTTPException
from typing import List
import asyncio


class DataHandler:
    def __init__(self):
        self.text = OpenAITextGeneration()
        self.voice = TextToSpeach()
        self.image = GenerateImage()
        self.messages = Messages()
        
    def handle_chat(self, content:str, role:str=None) -> str:
        role = role
        if not role:
            role = "user"
        if not role in ["user", "assistant", "system"]:
            role = "user"
        if not content:
            raise HTTPException(
                status_code=400, 
                detail="Content is required. Content is a string of text meant to be sent to the chat bot api."
                )
        messages = self.messages.create_message(role=role, content=content)
        messages = [self.messages.create_message(role=role, content=content)]
        return self.text.send_chat_complete(messages=messages)

    def handle_voice(self, message: str, voice_id: str) -> str:
        if not message:
            raise HTTPException(
                status_code=400, 
                detail="Message to be converted to speach required. Message is a string of text meant to be sent to the voice api."
                )
        if not voice_id:
            raise HTTPException(
                status_code=400,
                detail="Voice id is required. You can request voice options from /voice/options endpoint."
            )
        return self.voice.tts(text=message, voice_id=voice_id)
    
    def handle_image(self, prompt: str) -> str:
        if not prompt:
            raise HTTPException(
                status_code=400,
                detail="Prompt is required. Prompt is a string of text meant to be sent to the image api."
            )
        return asyncio.run(self.image.generate_image(prompt=prompt))
    
        


if __name__ == "__main__":
    asyncio.run(DataHandler())
