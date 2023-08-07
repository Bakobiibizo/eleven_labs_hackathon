
from voice_generation import VoiceGeneration


def run_voice_generation(text, voice_id):
    voice = VoiceGeneration()
    voice.generate_voice(text, voice_id)


if __name__ == "__main__":
    run_voice_generation(text=None, voice_id="D38z5RcWu1voky8WS1ja")


