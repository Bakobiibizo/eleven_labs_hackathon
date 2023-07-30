from data_handler import Tool, Info, DataHandler, OpenAITextGeneration
import json


class NarationTool(Tool):
    def __init__(self):
        super().__init__()
        self.name = "Naration Tool"
        self.image = OpenAITextGeneration()
        self.handler = DataHandler()

    def function(self, prompt):
        return self.handler.handle_narration(prompt=prompt)
    
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
This tool will update the narrator based on what just occured and what is is occuring in the game in the form of a prompt. It is important that you use this tool everytime the game state advances to a new stage. New characters appear, scenery changes, event occurs, etc. 
To use this tool respond with a json string in the following format:
{
    "command": "{self.name}",
    "prompt": "PROMPT"
}
Replace PROMPT with your prompt.
----EXAMPLE--------
{
    "command": "Naration Tool",
    "prompt": "The players just got attacked by a group of gangers in the street, and they need to find a way to escape."
}
----END EXAMPLE----
"""
        return description   
            
