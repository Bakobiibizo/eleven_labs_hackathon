import json
import os
from pydantic import BaseModel
import importlib

class Info(BaseModel):
    tool_name: str
    description: str
    command_string: str

class Tool:
    def __init__(self) -> None:
        self.name: str         
        
    def function(self, prompt: str) -> None:
        pass
    
    def description(self, prompt: str) -> str:
        pass
            
    def get_info(self) -> dict:
        pass
    
    
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
        
        

class ToolHandler(Tool):
    def __init__(self):
        super().__init__()
        self.command_executor = CommandExecutor()
        self.load_tools()
        
    def load_tools(self):
        for filename in os.listdir("tools"):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                tool_class_name = module_name.title().replace("_", "")
                module = importlib.import_module(f"tools.{module_name}")
                tool_class = getattr(module, tool_class_name)
                tool = tool_class()
                self.command_executor.register_tool(tool.name, tool)
                
    def function(self, json_command):
        return self.command_executor.execute_command(json_command)
    
    def description(self):
        description = f"""
You are a game master of an interactive RPG. Your task is to manage the game state and advance the story. Your focus can be on managing the game state. To help you, you have been provided a set of tools. These tools will help you generate narrative content, store and retrieve information, generate images and voice acting for the game. Use these tools and keep your focus on player stats, events in the game and the overarching story. You are not able to communicate with the players directly, but the tools will do that indirectly. Here is your list of tools:
    {[tool.get_info() for tool in self.command_executor.command_dispatcher.values()]}
    """
        return description

        