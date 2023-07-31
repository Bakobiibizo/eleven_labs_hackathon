from text.openai_text import OpenAITextGeneration
from text.create_messages import Messages
from voice.eleven_labs import TextToSpeach
from image.generate_image import GenerateImage
from text.context_window import ContextWindow
from tool_handler import ToolHandler
from fastapi import HTTPException, requests
import asyncio

class DataHandler:
    def __init__(self):
        self.context = ContextWindow(window_size=30)
        self.text = OpenAITextGeneration()
        self.voice = TextToSpeach()
        self.image = GenerateImage()
        self.messages = Messages()  
        self.tools = ToolHandler("Narrator")      
        
    def handle_chat(self, content:str, role:str=None) -> str:
        role = role
        if not role:
            role = "user"
        if not role in ["user", "assistant", "system"]:
            role = "user"
        if not content:
            raise HTTPException(
                status_code=400, 
                detail="Content is required. Content is a string of text meant to be sent to the chat bot api."
                )
        message = self.messages.create_message(role=role, content=content)
        self.context.add_message(message=message)
        messages = []
        for message in self.context.get_context():
            messages.append({
                "content": message.content,
                "role": message.role
            })
        assistant_message = self.text.send_chat_complete(messages=messages).choices[0].message
        assistant_message = self.update_image(assistant_message)
        self.context.add_message(message=assistant_message)
        return assistant_message.content

    def handle_voice(self, message: str, voice_id: str) -> str:
        if not message:
            raise HTTPException(
                status_code=400, 
                detail="Message to be converted to speach required. Message is a string of text meant to be sent to the voice api."
                )
        if not voice_id:
            raise HTTPException(
                status_code=400,
                detail="Voice id is required. You can request voice options from /voice/options endpoint."
            )
        return self.voice.tts(text=message, voice_id=voice_id)
    
    def handle_image(self, prompt: str) -> str:
        if not prompt:
            raise HTTPException(
                status_code=400,
                detail="Prompt is required. Prompt is a string of text meant to be sent to the image api."
            )
        return asyncio.run(self.image.generate_image(prompt=prompt))
    
    def update_image(self, prompt: str) -> str: 
        if not prompt:
            raise HTTPException(
                status_code=400,
                detail="Prompt is required. Prompt is a string of text meant to be sent to the image api."
            )
        for narrator in self.tools.command_executor.command_dispatcher.values():
            message = ""
            if narrator.name == "Narrator":
                message = self.tools.command_executor.execute_command(narrator.tool["Narrator"](prompt=prompt))
        image = asyncio.run(self.image.generate_image(prompt=prompt))
        body = {
            "imageString": image,
            "overlayText": message
        }
        return body
    
        
if __name__ == "__main__":
    asyncio.run(DataHandler())
