from pathlib import Path
import os 
from src.sambanova.api_client import SambanovaAPIClient
from src.sambanova.transcription import Transcription

def main() -> None:
    api_key = os.getenv("SN_API_KEY")
    if not api_key:
        raise ValueError("Missing SN_API_KEY environment variable")

    client = SambanovaAPIClient(api_key)

    # Path to your audio file
    audio_file_path = "examples/testdata/transcription/sample_audio2.mp3"  
    audio_file_name = os.path.basename(audio_file_path)
    model_name = "Whisper-Large-v3"

    print(f"Model: {model_name}\nAudio File: {audio_file_name} \nTranscribing audio (plain text response)...\n")
    text_response = Transcription.transcribe_audio_file(
        client,
        "Whisper-Large-v3",
        audio_file_path=audio_file_path,
        language="english",
        response_format="text",
        stream=False
    )
    print(text_response if isinstance(text_response, str) else text_response.get("text", ""))

if __name__ == "__main__":
    main()