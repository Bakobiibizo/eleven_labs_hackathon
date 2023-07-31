from tool_handler import ToolHandler
#from text.anthropic_text import AnthropicChatBot

class ContextWindow:
    def __init__(self, window_size=100):
        self.tool = ToolHandler(name="ContextWindow")
        self.window_size = window_size
        self.context = []

    def add_message(self, message):
        self.context.append(message)
        if len(self.context) > self.window_size:
            self.context.pop(0)

    def get_context(self):
        return self.context
    
    def start_context(self):
        return self.tool.get_message_by_type("Primer", "Context")
    
#    
#class AnthropicContext(ContextWindow):
#    def __init__(self, window_size=10000):
#        super().__init__(window_size)
#        self.tool = AnthropicChatBot()
#        self.window_size = window_size
#        self.context = []            