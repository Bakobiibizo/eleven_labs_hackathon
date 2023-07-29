import json
from urllib import request
import asyncio
import aiohttp

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
          
    def generate_image(self, prompt):
        self.prompt = json.loads(self.prompt_text)
        self.prompt["6"]["inputs"]["text"] = f"{prompt}, {self.style}"
        p = {"prompt": json.dumps(self.prompt)}
        data = json.dumps(p).encode('utf-8')
        req =  request.Request("http://127.0.0.1:8188/prompt", data=data)
        return req.data
    
    def set_style(self, style=None):
        if not style:
            style = """
            dramatic scene, anime style, ultra hd, realistic, vivid cyberpunk colors, highly detailed, UHD drawing, pen and ink, t-shirt design, illustration,
            """
        self.style = style
        return style
      
