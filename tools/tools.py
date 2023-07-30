import json
import os
from pydantic import BaseModel

class Tool(BaseModel):
    def __init__(self, name):
        self.name = name
    
    def function(self):
        pass
    
    def description(self):
        return self.description
        
    def get_info(self):
        return self.info
    
    
class CommandExecutor:
    def __init__(self):
        self.command_dispatcher = {}

    def register_tool(self, command_name, tool):
        self.command_dispatcher[command_name] = tool.function

    def execute_command(self, json_command):
        command = json.loads(json_command)
        function = self.command_dispatcher[command["command"]]
        result = function(command["prompt"])
        return result
        