from text.openai_text import OpenAITextGeneration
from text.create_messages import Messages, RoleOptions
from voice.eleven_labs import TextToSpeach
from image.generate_image import GenerateImage
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
        
    def generate_text(self, role: RoleOptions, content: str) -> str:
        if not role: 
            role = RoleOptions.USER
        prompt = [
            {
                "role": role,
                "content": content
            }
        ]
        response = self.text.send_chat_complete(prompt)
        res = response.choices[0].message.content
        print(res)
        return res


    def generate_voice(self, message: str, voice_id: str) -> str:
        base64_string = self.voice.tts(text=message, voice_id=voice_id)
        return base64_string
    
    async def generate_image(self, prompt: str=None) -> str:
        if not prompt:
            prompt = "a duck wearing a red fedora"
        image_ticket = self.generate_image(prompt)
        image_number = json.loads(image_ticket)["number"]+1
        image_id = json.loads(image_ticket)["prompt_id"]
        with open("image\image_ids.json", "r") as f:
            image_ids = json.load(f)
            if image_id not in [item['image_id'] for item in image_ids]:
                image_ids.append({'image_id': image_id, 'image_number': image_number})
                with open("image/image_ids.json", "w") as f:
                    json.dump(image_ids, f)
            else: 
                image_number = next((item['image_number'] for item in image_ids if item['image_id'] == image_id), None)

        png_count = len(glob.glob("D:/stable-diffusion-webui/comfyui/output/*.png"))

        image_number += png_count
        print(image_number)
        
        filename = f"D:/stable-diffusion-webui/ComfyUI/output/ComfyUI_{str(image_number).zfill(5)}_.png"
        print(filename)
    
        while not os.path.isfile(filename):
            await asyncio.sleep(1)  

        with open(filename, "rb") as f:
            image = f.read()
        image = Image.open(io.BytesIO(image))
        image.show()
        return image

if __name__ == "__main__":
    asyncio.run(DataHandler())
