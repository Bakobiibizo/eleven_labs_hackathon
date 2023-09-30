import os
import openai
from dotenv import load_dotenv
from text.create_messages import Messages
import json

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAITextGeneration:
    def __init__(self):
        self.messages = Messages()
        self.model = "gpt-3.5-turbo"
        self.chat = openai.ChatCompletion(model=self.model)

    def send_chat_complete(self, messages, model="gpt-3.5-turbo", role="user"):
        messages = self.messages.create_message(role=role, content=messages)
        try:
            print(messages)
            return self.chat.create(
                model=model,
                messages=messages,
            )
        except ConnectionError as e:
            print(f"There was an error connecting to OpenAI: {e}")
            raise

    def parse_openai_response(self, response):
        return response['choices'][0]['message']['content']