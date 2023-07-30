import os
import io
import json
import glob
import asyncio
from PIL import Image
from urllib import request



class GenerateImage:
    def __init__(self):
        self.prompt_text = """
{
    "3": {
        "class_type": "KSampler",
        "inputs": {
            "cfg": 8,
            "denoise": 1,
            "latent_image": [
                "5",
                0
            ],
            "model": [
                "4",
                0
            ],
            "negative": [
                "7",
                0
            ],
            "positive": [
                "6",
                0
            ],
            "sampler_name": "euler",
            "scheduler": "normal",
            "seed": 8566257,
            "steps": 20
        }
    },
    "4": {
        "class_type": "CheckpointLoaderSimple",
        "inputs": {
            "ckpt_name": "v1-5-pruned-emaonly.ckpt"
        }
    },
    "5": {
        "class_type": "EmptyLatentImage",
        "inputs": {
            "batch_size": 1,
            "height": 512,
            "width": 512
        }
    },
    "6": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [
                "4",
                1
            ],
            "text": "masterpiece best quality girl"
        }
    },
    "7": {
        "class_type": "CLIPTextEncode",
        "inputs": {
            "clip": [
                "4",
                1
            ],
            "text": "bad hands"
        }
    },
    "8": {
        "class_type": "VAEDecode",
        "inputs": {
            "samples": [
                "3",
                0
            ],
            "vae": [
                "4",
                2
            ]
        }
    },
    "9": {
        "class_type": "SaveImage",
        "inputs": {
            "filename_prefix": "ComfyUI",
            "images": [
                "8",
                0
            ]
        }
    }
}
"""
        self.style = self.set_style()
        
    def set_style(self, style=None):
        if not style:
            style = """
            dramatic scene, anime style, ultra hd, realistic, vivid cyberpunk colors, highly detailed, UHD drawing, pen and ink, t-shirt design, illustration,
            """
        self.style = style
        return style
          
    async def generate_image(self, prompt):
        self.prompt = json.loads(self.prompt_text)
        self.prompt["6"]["inputs"]["text"] = f"{prompt}, {self.style}"
        
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
            image = f.read()
        image = Image.open(io.BytesIO(image))
        image.show()
        return json.dumps(image)
    
    def set_style(self, style=None):
        if not style:
            style = """
            dramatic scene, anime style, ultra hd, realistic, vivid cyberpunk colors, highly detailed, UHD drawing, pen and ink, t-shirt design, illustration,
            """
        self.style = style
        return style
      
