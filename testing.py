#import asyncio
#import base64
#import io
#from pydub import playback
#from voice.eleven_labs import TextToSpeach
#from text.openai_text import OpenAITextGeneration
#from image.generate_image import GenerateImage
#from data_handler import DataHandler
from agents.narrator import Narrator
#from 
#handler = DataHandler()
#eleven = TextToSpeach()
#image = GenerateImage()
#text = OpenAITextGeneration()

#eleven.tts("welcome to the land of nerds", "tQGo4CObOu6hUEgRExhA")
#string = asyncio.run(image.generate_image(prompt="creepy house"))

#text.send_chat_complete(messages = [{"role": "user", "content": "Hi there how are you?"}])

#response = handler.handle_chat(role="user", content="Hi there how are you?")
#print(response)

#audio_data = handler.handle_voice(message="Hi there how are you?", voice_id="tQGo4CObOu6hUEgRExhA")
#print(audio_data)

#image = handler.handle_image(prompt="cat")
#print(image)


narrator = Narrator()
primer = narrator.get_primer()
print(primer)
