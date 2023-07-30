import json
from text.openai_text import OpenAITextGeneration
from text.create_messages import Messages
from text.context_window import ContextWindow
from tool_handler import ToolHandler


class NarroratorTool(ToolHandler):
    def __init__(self, name="NarratorTool"):
        super().__init__(name)
        self.name = name
        self.text = OpenAITextGeneration()
        self.messages = Messages()
        self.context = ContextWindow(window_size=30)
                
    def create_message(self, prompt: str) -> str:
        return self.messages.create_message(role="system", content=prompt)
            
    def command(self, prompt: str) -> str:
        return self.text.send_chat_complete(messages=self.create_message(role="system", content=prompt)).choices[0].message.content
    
    
class Narrator:
    def __init__(self):
        self.name = "Narrator"
        self.tool = NarroratorTool()
    
    def send_narration(self, prompt: str) -> str:
        primer = self.get_primer()
        context = self.get_context()
        prompt = f"{primer}\n {prompt}\n----\nPREVIOUS CONTEXT: {context}"
        return self.tool.command(json.load(prompt))
        
    def get_primer(self) -> str:
        with open ("agents/prompts.json", "r") as f:
            json_string = f.read()
            json_list = json.loads(json_string)
            if json_list[0]["message_type"] == "Narration" and json_list[0]["message_title"] == "Narrator":
                return json_list[0]["message"]["content"]
    
