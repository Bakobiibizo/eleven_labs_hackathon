import os
import io
import json
import requests
from dotenv import load_dotenv
from pydub import AudioSegment
from pydub.playback import play



load_dotenv()

class TextToSpeach():
    def __init__(self):
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
        self.url = f"{self.base_url}voices"
        self.data = None
        self.voices_request()

    def tts(self, text, voice_id):
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

        self.tts_request()

    def voices_request(self):
        response = requests.get(url=self.url, json=self.data, headers=self.headers)
        json_string = response.json()
        self.download_voices(json_string=json_string)

    def tts_request(self):
        response = requests.post(url=self.url, json=self.data, headers=self.headers, stream=True)
        audio_data = b""
        for chunk in response.iter_content(chunk_size=self.CHUNK_SIZE):
            audio_data += chunk

        # Convert binary data to an AudioSegment
        audio_file = io.BytesIO(audio_data)
        audio = AudioSegment.from_file(audio_file, format="mp3")

        # Play the audio
        play(audio)

    def download_voices(self, json_string):

        # Define your array of voice data
        with open("voice/voices.json", "r") as f:
            json_string = f.read()
            data_dict = json.loads(json_string)

        # Ensure the directory for voice samples exists
        os.makedirs('voice/voice_samples', exist_ok=True)

        # Iterate over the voice data
        for voice in data_dict['voices']:
            name = voice['name']
            voice_id = voice['voice_id']
            url = voice['preview_url']

            # Use requests to download the file
            response = requests.get(url)
            if response.status_code != 200:
                continue

            # Check if the request was successful
            if response.status_code == 200:
                # Create the filename
                filename = f'voice/voice_samples/{name}_{voice_id}.mp3'

                # Write the content to a file
                with open(filename, 'wb') as f:
                    f.write(response.content)
