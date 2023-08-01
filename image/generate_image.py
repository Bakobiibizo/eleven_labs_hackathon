import asyncio
import base64
import json
import os
from urllib import request
from logger import debug_logger

logger = debug_logger


class GenerateImage:
    def __init__(self):
        self.prompt = None
        self.image_primer = None
        self.theme = None
        self.image_ids = None
        self.set_image_primer()
        self.get_theme()
        self.style = None
        self.image_count = 0

    def get_theme(self):
        with open("image/theme.json", "r") as f:
            self.theme = f.read()
            logger.log(level=10, msg=self.theme)
            return json.loads(self.theme)
        
    def set_style(self, style=None):
        if not style:
            style = """dramatic scene, anime style, ultra hd, realistic, vivid cyberpunk colors, highly detailed, 
            UHD drawing, pen and ink, t-shirt design, illustration,"""
        self.style = style
        logger.log(level=10, msg=self.style)
        return style

    def set_image_primer(self, image_primer=None):
        if not image_primer:
            image_primer = """dramatic scene, anime style, ultra hd, realistic, vivid cyberpunk colors, 
            highly detailed, UHD drawing, pen and ink, t-shirt design, illustration,"""
        self.image_primer = image_primer
        logger.log(level=10, msg=self.image_primer)
        return image_primer
    
    def set_prompt(self, prompt):
        logger.log(level=10, msg=prompt)
        try:
            self.theme = self.get_theme()  # Ensure self.theme is a valid dictionary
            self.theme["87"]["inputs"]["text_positive"] = f"{str(prompt)}, {str(self.image_primer)}"
            logger.log(level=10, msg=self.theme)
        except KeyError as e:
            print(f"Error accessing theme data: {e}")
        except json.JSONDecodeError as e:
            print(f"Error parsing theme data as JSON: {e}")
        self.prompt = self.theme
        logger.log(level=10, msg=self.prompt)
        return self.prompt


    async def generate_image(self, prompt, style=None, image_primer=None):
        self.set_image_primer(image_primer=image_primer)
        self.get_theme()
        self.set_style(style=style)

        self.prompt = self.set_prompt(prompt)

        p = {"prompt": self.prompt}
        print(self.prompt)
        data = json.dumps(p).encode('utf-8')
        image_data = None

        try:
            req = asyncio.run(request.Request("http://127.0.0.1:8188/prompt", data=data))
            image_data = await json.loads(request.urlopen(req).read())

            if 'error' in image_data or 'false' in image_data['success']:
                raise Exception('Error or false success in image generation')
        except Exception as e:
            print(f'Error in image generation: {e}. Retrying...')

        self.image_count += 1
        image_number = self.image_count
        image_id = image_data["prompt_id"]
        with open("image/image_ids.json", "r") as f:
            image_ids = json.load(f)
            if image_id not in [item['image_id'] for item in image_ids]:
                image_ids.append({'image_id': image_id, 'image_number': image_number})
                with open("image/image_ids.json", "w") as file:
                    json.dump(image_ids, file)

        filename = f"D:/stable-diffusion-webui/ComfyUI/output/ComfyUI_{str(image_number).zfill(5)}_.png"
        print(filename)

        for _ in range(self.MAX_RETRIES):
            if os.path.isfile(filename):
                break
            asyncio.run(asyncio.sleep(1))
        else:
            print('Failed to find image file after maximum number of retries')
            return None

        with open(filename, "rb") as f:
            image_data = f.read()
        # Encode the binary data to base64
        encoded_image_data = base64.b64encode(image_data)
        # Convert the base64 bytes to string
        serialized_image = encoded_image_data.decode('utf-8')
        return serialized_image


