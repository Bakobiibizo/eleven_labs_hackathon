from data_handler import Tool, Info, DataHandler, GenerateImage
import json


class ImageTool(Tool):
    def __init__(self):
        super().__init__()
        self.name = "Image Tool"
        self.image = GenerateImage()
        self.handler = DataHandler()

    def function(self, prompt):
        return self.handler.handle_image(prompt=prompt)
    
    def get_info(self):
        info = Info(
            tool_name = self.name,
            description = self.description(),
            json_command_string = f"""{
                'name': {self.name},
                'command': {json.dumps(self.function)}
            }"""
        ).dict()
        return info
    
    def description(self):
        description = f"""
This tool will update the splash art of the game based on a prompt. It is important that you use this tool everytime the game state advances to a new stage. New characters appear, scenery changes, event occurs, etc. Describe the scene in the form of a prompt. Focus on being detailed about the subject of the image and the scene the style and coloring have been taken care of already. Be descriptive and use flourishing language but do not be overly verbose. Sperate subject and verb with a comma.
To use this tool respond with a json string in the following format:
{
    "command": "{self.name}",
    "prompt": "PROMPT"
}
Replace PROMPT with your prompt.
----EXAMPLE--------
{
    "command": "Image Tool",
    "prompt": "A grizzled old, sitting in an alley, sheltering under a newspaper, cigarette dangling from his mouth. he is wearing a long trench coat and a fedora, he is holding a revolver in his right hand."
}
----END EXAMPLE----
"""
        return description   