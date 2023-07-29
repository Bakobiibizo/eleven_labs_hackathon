import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAITextGeneration:
    def __init__(self):
        pass

    async def send_chat_complete(self, messages):
        try:
            responses = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo", messages=messages, stream=True
            )
            for response in responses:
                full_response += response.choices[0].message['content']
            print(full_response)
            return full_response
        except ConnectionError as e:
            print(f"There was an error connecting to OpenAI: {e}")
            raise