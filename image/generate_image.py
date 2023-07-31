import os
import json
import glob
import asyncio
from urllib import request
import base64



class GenerateImage:
    def __init__(self):
        self.prompt_text 
        
    def get_theme(self):
        with open("image/theme.json", "r" ) as f:
            self.theme=json.load(f)
            return json.load(f)
            
    def set_image_primer(self, image_primer=None):
        if not image_primer:
            image_primer = """
            dramatic scene, anime style, ultra hd, realistic, vivid cyberpunk colors, highly detailed, UHD drawing, pen and ink, t-shirt design, illustration,
            """
        self.image_primer = image_primer
        return image_primer
          

    async def generate_image(self, prompt):
        self.prompt = json.loads(self.prompt_text)
        self.prompt["87"]["text_positive"]["text"] = f"{prompt}, {self.image_primer}"
        
        p = {"prompt": self.prompt}
        data = json.dumps(p).encode('utf-8')
        
        req =  request.Request("http://127.0.0.1:8188/prompt", data=data)
        
        image_data = json.loads(request.urlopen(req).read())
        image_number = image_data["number"]+1
        image_id = image_data["prompt_id"]
        
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
            image_data = f.read()
        # Encode the binary data to base64
        encoded_image_data = base64.b64encode(image_data)
        # Convert the base64 bytes to string
        serialized_image = encoded_image_data.decode('utf-8')
        return serialized_image
    
    def set_style(self, style=None):
        if not style:
            style = """
            dramatic scene, anime style, ultra hd, realistic, vivid cyberpunk colors, highly detailed, UHD drawing, pen and ink, t-shirt design, illustration,
            """
        self.style = style
        return style
      
