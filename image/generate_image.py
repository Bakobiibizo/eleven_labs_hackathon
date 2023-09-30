import asyncio
import base64
import json
import os
from urllib import request
import asyncio as asyncio


class GenerateImage:
    def __init__(self):
        self.prompt = None
        self.image_primer = None
        self.theme = None
        self.image_ids = None
        self.set_image_primer()
        self.get_theme()
        self.style = None

    def get_theme(self):
        with open("image/theme.json", "r") as f:
            self.theme = f.read()
            return json.loads(self.theme)

    def set_image_primer(self, image_primer=None):
        if not image_primer:
            image_primer = """dramatic scene, anime style, ultra hd, realistic, vivid cyberpunk colors, 
            highly detailed, UHD drawing, pen and ink, t-shirt design, illustration,"""
        self.image_primer = image_primer
        return image_primer

    def count_down(self, filename):
        for _ in range(60):
            if os.path.isfile(filename):
                break
            asyncio.run(asyncio.sleep(1))
        else:
            print('Failed to find image file after maximum number of retries')
            return None

    image_count = 0  # Class variable to keep track of the number of images generated

    def generate_image(self, prompt):
        print(f"Prompt before JSON loading: {prompt}")
        if not prompt:
            raise ValueError("prompt is required")
        self.prompt = prompt
        with open("image/theme.json", "r") as theme:
            self.theme = json.load(theme)
        print(self.theme)
        self.theme["87"]["inputs"]["text_positive"] = f"{self.prompt}, {self.image_primer}"

        p = {"prompt": self.prompt}
        data = json.dumps(p).encode('utf-8')

        try:
            req = request.Request("http://127.0.0.1:8188/prompt", data=data)
            image_data = json.loads(request.urlopen(req).read())
            self.count_down(filename=filename)
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



        with open(filename, "rb") as f:
            image_data = f.read()
        # Encode the binary data to base64
        encoded_image_data = base64.b64encode(image_data)
        return encoded_image_data.decode('utf-8')

    def set_style(self, style=None):
        if not style:
            style = """dramatic scene, anime style, ultra hd, realistic, vivid cyberpunk colors, highly detailed, 
            UHD drawing, pen and ink, t-shirt design, illustration,"""
        self.style = style
        return style
