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
import os
import glob

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
        image_data = self.image.generate_image(prompt)
        return image_data
    


async def test():
    handler = DataHandler()
    # Set a timeout for the image generation
    image_ticket = handler.generate_image("a duck wearing a fedora")
    image_number = json.loads(image_ticket)
    image = await asyncio.wait_for(image_number, timeout=300)
    print(image)
    
    # Count the number of PNG files in the directory
    png_count = len(glob.glob("D:/stable-diffusion-webui/comfyui/output/*.png"))
    # Add the count to the image number
    image = png_count
    # Generate the new filename
    filename = f"ComfyUI_{str(image).zfill(5)}.png"
    
    # Wait until the file is generated
    with not os.path.isfile(filename):
        await asyncio.sleep(1)  # wait for 1 second before checking again
    
    with open(filename, "rb") as f:
        image = f.read()
    image = Image.open(io.BytesIO(image))
    image.show()
#    haiku = handler.generate_text("user", "write a haiku about a duck wearing a fedora")
#    print(haiku.content)
#    audio = handler.generate_voice(haiku.content, "tQGo4CObOu6hUEgRExhA")
#    play(audio)

if __name__ == "__main__":
    asyncio.run(test())
