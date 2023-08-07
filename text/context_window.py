import json

class ContextWindow:
    def __init__(self, window_size=100):
        self.window_size = window_size
        self.context = []

    def add_message(self, message):
        self.context.append(message)
        if len(self.context) > self.window_size:
            self.context.pop(0)

    def get_context(self):
        return self.context
    
    def start_context(self):
        with open("text/prompts.json", "r", encoding="utf-8") as f:
            json_string = f.read()
            print(json_string)
            for message in json_string[-self.window_size]:
                self.add_message(message[0]["message_title"][""])
        return self.context
    
#    
#class AnthropicContext(ContextWindow):
#    def __init__(self, window_size=10000):
#        super().__init__(window_size)
#        self.tool = AnthropicChatBot()
#        self.window_size = window_size
#        self.context = []            