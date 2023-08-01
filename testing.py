from text.openai_text import OpenAITextGeneration
from image.generate_image import GenerateImage
from voice.eleven_labs import TextToSpeach
from pydub.playback import play
from logger import debug_logger
import asyncio

logger = debug_logger


class Test():
    def __init__(self):
        self.text = OpenAITextGeneration()
        self.image = GenerateImage()
        self.voice = TextToSpeach()

    def test_image(self):
        image_data = self.image.generate_image("a hacker encountering a firewall in cyberspace")
        logger.log(level=10, msg=image_data)
        return image_data

    def test_text(self):
        messages = [{
            "role": "user",
            "content": " this is the content"
        }]
        response = self.text.send_chat_complete(messages)
        logger.log(level=10, msg=response)
        return response

    def test_voice(self):
        prompt = "this is a test of the server"
        voice_id = "AZnzlk1XvdvUeBnXmlld"
        byte_string = self.voice.tts(text=prompt, voice_id=voice_id)
        play(byte_string)
        logger.log(level=10, msg=byte_string)
        with open('output/output.mp3', 'wb') as f:
            f.write(byte_string)
        print("Voice has been saved to output/output.mp3")
        return "success"



def run_test_async():
    test = Test()
    test.test_image()

run_test_async()
