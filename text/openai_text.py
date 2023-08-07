import json
import os
import openai
from dotenv import load_dotenv
from text.create_messages import Messages

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAITextGeneration:
    def __init__(self):
        self.openai_chat = Messages()

    def send_chat_complete(self, content, model="gpt-3.5-turbo", role="user"):
        try:
            message = self.messages.create_message(role=role, content=content)
            messages = []
            for message in self.context.get_context():
                messages.append(json.loads(message.content))            
            response = openai.ChatCompletion.create(
                model, messages=messages, stream=True
            )
            return response
        except ConnectionError as e:
            print(f"There was an error connecting to OpenAI: {e}")
            raise