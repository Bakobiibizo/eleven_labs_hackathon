import os
import io
import json
import requests
import base64
from dotenv import load_dotenv
from pydub import AudioSegment
from voices import Voices
from pydub.playback import play

load_dotenv()

class VoiceGeneration():
    """
    A class for generating voices using the Eleven Labs API.

    Attributes:
    - url (str): The URL for the API endpoint.
    - data (dict): The data to be sent in the API request.
    - CHUNK_SIZE (int): The chunk size for streaming audio data.
    - base_url (str): The base URL for the Eleven Labs API.
    - api_key (str): The API key for Eleven Labs.
    - headers (dict): The headers to be sent in the API request.
    """

    def __init__(self):
        """
        Initializes a new instance of the VoiceGeneration class.
        """
        self.url = None
        self.data = None
        self.CHUNK_SIZE = 1024
        self.base_url = "https://api.elevenlabs.io/v1/"
        self.api_key = os.environ.get("ELEVEN_LABS_API_KEY")
        self.headers = {
          "Accept": "audio/mpeg",
          "Content-Type": "application/json",
          "xi-api-key": self.api_key
        }

    def voices(self):
        """
        Sends a GET request to the Eleven Labs API to retrieve a list of available voices.
        """
        self.url = f"{self.base_url}voices"
        self.data = None
        self.voices_request()

    def generate_voice(self, text, voice_id):
        """
        Sends a POST request to the Eleven Labs API to generate an audio file for the given text and voice ID.

        Args:
        - text (str): The text to be converted to speech.
        - voice_id (str): The ID of the voice to be used for the speech.

        Returns:
        - audio_data (bytes): The audio data in MP3 format.
        """
        if not voice_id:
            voice_id = None
        if not text:
            raise ValueError("text is required")
        self.url = f"{self.base_url}text-to-speech/{voice_id}/stream"
        self.data = {
          "text": text,
          "model_id": "eleven_monolingual_v1",
          "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
          }
        }
        audio_data = self.tts_request()
        if isinstance(audio_data, str):
            audio_data = audio_data.encode('utf-8')
        return audio_data

    def voices_request(self):
        """
        Sends a GET request to the Eleven Labs API to retrieve a list of available voices.
        """
        response = requests.get(url=self.url, json=self.data, headers=self.headers)
        json_string = response.json()
        self.download_voices(json_string=json_string)            

    def tts_request(self):
        """
        Sends a POST request to the Eleven Labs API to generate an audio file for the given text and voice ID.

        Returns:
        - base64_string (str): The base64-encoded audio data in MP3 format.
        """
        response = requests.post(url=self.url, json=self.data, headers=self.headers, stream=True)
        audio_data = b""
        for chunk in response.iter_content(chunk_size=self.CHUNK_SIZE):
            audio_data += chunk
    
        audio = AudioSegment.from_file(io.BytesIO(audio_data), format="mp3")
        
        with open("output/voice.mp3", "wb") as f:
            f.write(audio_data)
        play("output/voice.mp3")
        byte_string = io.BytesIO()
        audio.export(byte_string, format="mp3")
        base64_string = base64.b64encode(byte_string.getvalue()).decode("utf-8")
        
        return base64_string

    def download_voices(self, json_string):
        """
        Downloads voice samples for the available voices from the Eleven Labs API.

        Args:
        - json_string (str): The JSON string containing the available voices.
        """
        data_dict = []

        with open("voices.json", "r") as f:
            json_string = f.read()
            data_dict = json.loads(json_string)

        os.makedirs('voice/voice_samples', exist_ok=True)

        voice_choice = Voices()
        for voice in data_dict['voices']:
            name = voice['name']
            voice_id = voice['voice_id']
            url = voice['preview_url']
            age = voice['labels'].get('age')
            gender = voice['labels'].get('gender')
            use_case = voice['labels'].get('use case')
            accent = voice['labels'].get('accent')
            description = voice.get('description')
            
            name = name.replace(" ", "_")
            
            voice_choice.add(voice=Voices(name=name, voice_id=voice_id, accent=accent, description=description, age=age, gender=gender, use_case=use_case))
                       
            response = requests.get(url)
            if response.status_code != 200:
                continue
            if response.status_code == 200:
                filename = f'voice/voice_samples/{name}_{voice_id}.mp3'

                with open(filename, 'wb') as f:
                    f.write(response.content)

if __name__ == "__main__":
   voice = VoiceGeneration()
   response = voice.generate_voice(text="hello", voice_id="D38z5RcWu1voky8WS1ja")