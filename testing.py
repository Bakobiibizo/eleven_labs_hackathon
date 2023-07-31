##import json
#import asyncio
##import base64
##import io
##from pydub import playback
##from voice.eleven_labs import TextToSpeach
##from text.openai_text import OpenAITextGeneration
#from text.create_messages import Message
##from image.generate_image import GenerateImage
##from data_handler import DataHandler
##from agents.narrator import Narrator
#from text.anthropic_text import AnthropicChatBot
#from text.anthropic_text import PromptConverter
#from typing import Dict
#
#
##from 
##handler = DataHandler()
##eleven = TextToSpeach()
##image = GenerateImage()
##text = OpenAITextGeneration()
#
##eleven.tts("welcome to the land of nerds", "tQGo4CObOu6hUEgRExhA")
##string = asyncio.run(image.generate_image(prompt="creepy house"))
#
##text.send_chat_complete(messages = [{"role": "user", "content": "Hi there how are you?"}])
#
##response = handler.handle_chat(role="user", content="Hi there how are you?")
##print(response)
#
##audio_data = handler.handle_voice(message="Hi there how are you?", voice_id="tQGo4CObOu6hUEgRExhA")
##print(audio_data)
#
##image = handler.handle_image(prompt="cat")
##print(image)
#
##prompt="the players got pulled over by the police, they sitting in the car as the police officer walks up, day time"
##narrator = Narrator()
##primer = narrator.get_primer()
##context = narrator.tool.command(prompt)
##print(context)
#
#
#async def anthropic_chat():
#    
#    anthropic = AnthropicChatBot()
#    converter = PromptConverter()
#    message= Message(role = "user", content = "Hi there how are you?").dict()
#    message = converter.convert_to_anthropic(message_dict=[message])
#    print(message)
#    return await anthropic.generate_prompt(prompt=[message])
#    
#print(asyncio.run(anthropic_chat()))
#

