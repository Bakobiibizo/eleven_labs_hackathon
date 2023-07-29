import json
from urllib import request

class ImagePrompt:
    def __init__(self):
        self.style = self.set_style()
        self.prompt_template = json.loads(self.prompt_template())
        self.prompt = None
    
    def get_prompt(self, prompt):
        self.prompt = self.prompt_template      
        self.prompt["84"]["inputs"]["prompt"] = prompt + self.style
        return self.prompt
    
    def set_style(style=None):
        if not style:
            style = """
            dramatic scene, anime style, ultra hd, realistic, vivid cyberpunk colors, highly detailed, UHD drawing, pen and ink, t-shirt design, illustration,
            """
        style = style
        return style
      
    def queue_prompt(self, prompt):
        p = {"prompt": prompt}
        data = json.dumps(p).encode('utf-8')
        req =  request.Request("http://127.0.0.1:8188/prompt", data=data)
        request.urlopen(req)
    
    def prompt_template(self):
        prompt_text = """
{
  "5": {
    "inputs": {
      "ckpt_name": "stable-diffusion-xl-base-1.0/sd_xl_base_1.0.safetensors"
    },
    "class_type": "CheckpointLoaderSimple"
  },
  "8": {
    "inputs": {
      "ckpt_name": "stable-diffusion-xl-refiner-1.0/sd_xl_refiner_1.0.safetensors"
    },
    "class_type": "CheckpointLoaderSimple"
  },
  "19": {
    "inputs": {
      "width": 1024,
      "height": 1024,
      "batch_size": 1
    },
    "class_type": "EmptyLatentImage"
  },
  "28": {
    "inputs": {
      "samples": [
        "33",
        0
      ],
      "vae": [
        "79",
        0
      ]
    },
    "class_type": "VAEDecode"
  },
  "33": {
    "inputs": {
      "noise_seed": 531611176769857,
      "steps": 50,
      "cfg": 25,
      "sampler_name": "dpmpp_2m_sde_gpu",
      "scheduler": "karras",
      "base_ratio": 0.85,
      "denoise": 1,
      "base_model": [
        "82",
        0
      ],
      "base_positive": [
        "67",
        0
      ],
      "base_negative": [
        "67",
        1
      ],
      "refiner_model": [
        "8",
        0
      ],
      "refiner_positive": [
        "67",
        2
      ],
      "refiner_negative": [
        "67",
        3
      ],
      "latent_image": [
        "19",
        0
      ]
    },
    "class_type": "SeargeSDXLSampler"
  },
  "67": {
    "inputs": {
      "pos_g": [
        "84",
        0
      ],
      "pos_l": [
        "84",
        0
      ],
      "pos_r": [
        "84",
        0
      ],
      "neg_g": [
        "72",
        0
      ],
      "neg_l": [
        "72",
        0
      ],
      "neg_r": [
        "72",
        0
      ],
      "base_width": 1024,
      "base_height": 1024,
      "crop_w": 0,
      "crop_h": 0,
      "target_width": 1024,
      "target_height": 1024,
      "pos_ascore": 8,
      "neg_ascore": 2,
      "refiner_width": 1024,
      "refiner_height": 1024,
      "base_clip": [
        "82",
        1
      ],
      "refiner_clip": [
        "78",
        0
      ]
    },
    "class_type": "SeargeSDXLPromptEncoder"
  },
  "72": {
    "inputs": {
      "prompt": "ugly, poorly drawn hands, missing limb, over saturated, grain, blurry, bad anatomy, disfigured, poorly drawn face, mutation, disconnected limbs, out of focus, long body, disgusting, poorly drawn, mutilated, mangled, extra fingers, gross proportions, missing arms, mutated hands, cloned face, missing legs, watermarks"
    },
    "class_type": "SeargePromptText"
  },
  "75": {
    "inputs": {
      "filename_prefix": "ComfyUI",
      "images": [
        "28",
        0
      ]
    },
    "class_type": "SaveImage"
  },
  "77": {
    "inputs": {
      "clip_name1": "base_text_encoder/model.safetensors",
      "clip_name2": "base_text_encoder_2/model.safetensors"
    },
    "class_type": "DualCLIPLoader"
  },
  "78": {
    "inputs": {
      "clip_name": "text_encoder_2/model.safetensors"
    },
    "class_type": "CLIPLoader"
  },
  "79": {
    "inputs": {
      "vae_name": "sdxl-vae/diffusion_pytorch_model.safetensors"
    },
    "class_type": "VAELoader"
  },
  "82": {
    "inputs": {
      "lora_name": "sd_xl_offset_example-lora_1.0.safetensors",
      "strength_model": 1,
      "strength_clip": 1,
      "model": [
        "5",
        0
      ],
      "clip": [
        "77",
        0
      ]
    },
    "class_type": "LoraLoader"
  },
  "84": {
    "inputs": {
      "prompt": "Grimm’s Bedtime story book cover, two sides, chromolithography, half side is a cold crooked enchanted creepy forest in the style of Over the garden Wall, as old weird vintage post cards , extreme high contrast, black and white, only one glowing complementary color red, orange, yellow fire lantern provide light on a small castle, small boy in the distance path, accentuate black lines, 8k resolution, professional, black dark forest, cup head style, pitch black, unsettling shadows,"
    },
    "class_type": "SeargePromptText"
  }
}
"""
        return prompt_text
      
