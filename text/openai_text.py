import os
import openai
from dotenv import load_dotenv
from text.create_messages import Messages

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAITextGeneration:
    def __init__(self):
        self.openai_chat = Messages()

    def send_chat_complete(self, messages, model="gpt-3.5-turbo"):
        self.messages= messages
        self.model = model
        try:
            formatted_messages = []
            for message in self.messages:
                formatted_messages.append(message)
            print(formatted_messages, self.model)
            response = openai.ChatCompletion.create(
                model=self.model, 
                messages=formatted_messages, 
                stream=True
            )
            return response
        except ConnectionError as e:
            print(f"There was an error connecting to OpenAI: {e}")
            raise

    def parse_openai_response(self, response):
        return response['choices'][0]['message']['content']