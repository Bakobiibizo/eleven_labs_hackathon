from text.openai_text import OpenAITextGeneration
from image.generate_image import GenerateImage
from voice.eleven_labs import TextToSpeach
import base64


class Test:
    def __init__(self):
        self.text = OpenAITextGeneration()
        self.image = GenerateImage()
        self.voice = TextToSpeach()

    def test_image(self):
        image_data = self.image.generate_image("a hacker encountering a firewall in cyberspace")
        print(image_data)
        return image_data

    def test_text(self):
        messages = [{
            "role": "user",
            "content": " this is the content"
        }]
        response = self.text.send_chat_complete(messages)
        print(response)
        return response

    def test_voice(self):
        prompt = "this is a test of the server"
        voice_id = "AZnzlk1XvdvUeBnXmlld"
        byte_string = self.voice.tts(text=prompt, voice_id=voice_id)

        base64_string = base64.b64decode(byte_string.getvalue()).encode("utf-8")
        audio.export(byte_string, format="mp3")


Test()
