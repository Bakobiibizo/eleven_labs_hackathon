from image.generate_image import GenerateImage
from tools.tools import Tool

class ImageTool(Tool):
    def __init__(self, name):
        super().__init__(name)
        self.image = GenerateImage()

    def function(self, prompt):
        return self.image.generate_image(prompt=prompt)
    
    def description(self):
        description = """
This tool allows you to generate an image from a prompt. Use natural language to describe the scene that the players are in. Shorter is better. Focus on the subjects of the image and the location they are in, the styling and color of the image have been handled already. To use this tool respond with a json string in the following format:
"""
        return description    