from data_handler import Tool, Info, DataHandler, OpenAITextGeneration
import json


class VoiceTool(Tool):
    def __init__(self):
        super().__init__()
        self.name = "Voice Tool"
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
This tool will provide voice acting for narration and characters in the game by sending a prompt with the dialogue. It is important that you use this tool everytime the game state advances to a new stage. New characters appear, scenery changes, event occurs, etc. 
You have a choice of available voices
To use this tool respond with a json string in the following format:
{
    "command": "{self.name}",
    "prompt": "PROMPT"
}
Replace PROMPT with your prompt.
----EXAMPLE--------
{
    "command": "Voice Tool",
    "voice_id": "tQGo4CObOu6hUEgRExhA",
    "voice_of": "the bartender"
    "prompt": "Welcome, to data spike gents, can I get you something to drink?"
}
----END EXAMPLE----
"""
        return description   
            