import json
from text.parse_context_memory import parse_messages


class ContextWindow:
    def __init__(self, window_size=100):
        self.memory_path = "text/context_memory.json"
        self.window_size = window_size
        self.context = []
        self.parse = parse_messages

    def add_message(self, message):
        self.context.append(message)
        if len(self.context) > self.window_size:
            self.context.pop(0)

    def get_context(self):
        return self.context
    
    def start_context(self):
        message_history = self.parse(self.memory_path)
        for message in message_history:
            json.loads(message)
            self.add_message(message)
            print(message)
        self.check_length()
        return self.context
    
    def check_length(self):
        while len(self.context) > self.window_size:
            self.context.pop(0)
            
        
            
        
    
#    
#class AnthropicContext(ContextWindow):
#    def __init__(self, window_size=10000):
#        super().__init__(window_size)
#        self.tool = AnthropicChatBot()
#        self.window_size = window_size
#        self.context = []            