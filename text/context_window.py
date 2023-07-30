class ContextWindow:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.context = []

    def add_message(self, message):
        self.context.append(message)
        if len(self.context) > self.window_size:
            self.context.pop(0)

    def get_context(self):
        return self.context