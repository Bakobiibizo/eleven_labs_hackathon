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

        audio_file = io.BytesIO(audio_data)
        audio = AudioSegment.from_file(audio_file, format="mp3")
        return audio

    def download_voices(self, json_string):
        data_dict = []

        with open("voice/voices.json", "r") as f:
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
            
            voice_choice.add(voice=Voice(name=name, voice_id=voice_id, accent=accent, description=description, age=age, gender=gender, use_case=use_case))
                       
#            response = requests.get(url)
#            if response.status_code != 200:
#                continue

#            if response.status_code == 200:
#                filename = f'voice/voice_samples/{name}_{voice_id}.mp3'

#                with open(filename, 'wb') as f:
#                    f.write(response.content)


def test():
    eleven = TextToSpeach()
    eleven.tts("I will tell you a tale about a duck wearing a fedora", "tQGo4CObOu6hUEgRExhA")

if __name__ == "__main__":
    test()
    