import json
from pydantic import BaseModel

class Info(BaseModel):
    tool_name: str
    description: str
    command_string: str

class Tool:
    def __init__(self, name: str) -> None:
        self.name = name

    def function(self, prompt: str) -> None:
        raise NotImplementedError

    def description(self) -> str:
        raise NotImplementedError

    def get_info(self) -> Info:  
        raise NotImplementedError  
    
    def command(self) -> str:  
        raise NotImplementedError

class CommandExecutor:
    def __init__(self):
        self.command_dispatcher = {}

    def register_tool(self, command_name: str, tool: Tool):  
        self.command_dispatcher[command_name] = tool.function

    def execute_command(self, json_command: str):  
        command = json.loads(json_command)
        function = self.command_dispatcher[command["command"]]
        result = function(command["prompt"])
        return result

class ToolHandler(Tool):
    def __init__(self, name: str):  
        super().__init__(name)
        self.command_executor = CommandExecutor()

    def load_tools(self, name: str, function):  
        self.command_executor.register_tool(name, function)

    def function(self, json_command: str):  
        return self.command_executor.execute_command(json_command)

    def description(self, name: str) -> str:  
        json_description = self.get_message_by_type("Description", name)
        description =f"""
{json_description}
{[tool.get_info() for tool in self.command_executor.command_dispatcher.values()]}
        """
        return description.replace("\\n", "\n")

    @staticmethod
    def get_message_by_type(message_type: str, message_title: str) -> dict:
        with open ("agents/prompts.json", "r") as f:
            json_string = f.read()
            json_list = json.loads(json_string)
        for obj in json_list:
            if obj["message_type"] == message_type and obj["message_title"] == message_title:
                message = obj["message"]
                if isinstance(message, dict):
                    return {
                        "Role": message["role"],
                        "Content": message["content"]
                    }
                else:
                    return {
                        "Message": message["content"]
                    }

    def json_command(self, name: str, command: str) -> str:  
        json_command_string = json.dumps({
            'name': name,
            'command': command
        })
        return json_command_string

    def get_info(self, name: str, description: str, command: str) -> dict: 
        info = Info(
            tool_name = name,
            description = description,
            json_command_string = self.json_command(name, command)
        )
        return info.model_dump() 
    def command(self, ):
        return 
