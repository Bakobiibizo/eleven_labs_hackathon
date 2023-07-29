from text.openai_text import OpenAITextGeneration
from text.create_messages import Messages, RoleOptions, Message
from voice.eleven_labs import TextToSpeach
from image.generate_image import GenerateImage
from typing import List, Dict
from pydub.playback import play
from PIL import Image
import asyncio
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
    
    async def generate_image(self, prompt: str) -> str:
        image_data = await self.image.generate_image(prompt)
        return image_data
    
async def test():
    handler = DataHandler()
    image_ticket = await handler.generate_image("a duck wearing a fedora")
    image_number = image_ticket["number"]
    #I need to check "D:/stable-diffusion-webui/comfyui/output" and count how many png files there are and then add that number to the image number to get the correct file. then grab it in the format ComfyUI_{number preceeded by 0s until there are 5 digits}.png once the image is generated
    print("Image saved to image.jpg")
#    haiku = handler.generate_text("user", "write a haiku about a duck wearing a fedora")
#    print(haiku.content)
#    audio = handler.generate_voice(haiku.content, "tQGo4CObOu6hUEgRExhA")
#    play(audio)

if __name__ == "__main__":
    asyncio.run(test())
