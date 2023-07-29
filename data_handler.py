from text.openai_text import OpenAITextGeneration
from text.create_messages import Messages, RoleOptions, Message
from voice.eleven_labs import TextToSpeach
from image.generate_image import GenerateImage
from typing import List, Dict
from pydub.playback import play
from PIL import Image
import io
import json

class DataHandler:
    def __init__(self):
        self.text = OpenAITextGeneration()
        self.voice = TextToSpeach()
        self.image = GenerateImage()
        self.messages = Messages()
        
    def generate_text(self, role: RoleOptions, content: str) -> List[str]:
        if not role: 
            role = RoleOptions.USER
        prompt = [
            {
                "role": role,
                "content": content
            }
        ]
        response = self.text.send_chat_complete(prompt)
        res = response.choices[0].message
        print(res)
        return res


    def generate_voice(self, message: str, voice_id: str) -> str:
        audio_file = self.voice.tts(text=message, voice_id=voice_id)
        return audio_file
    
    def generate_image(self, prompt: str) -> str:
        prompt = self.image.get_prompt(prompt)
        image = self.image.queue_prompt(prompt)
        return image
    
def test():
    handler = DataHandler()
    #image_data = await handler.generate_image("a duck wearing a fedora")
    #image = Image.open(io.BytesIO(image_data))
    #image.show()
    haiku = handler.generate_text("user", "write a haiku about a duck wearing a fedora")
    print(haiku.content)
    audio = handler.generate_voice(haiku.content, "tQGo4CObOu6hUEgRExhA")
    play(audio)

if __name__ == "__main__":
    test()
