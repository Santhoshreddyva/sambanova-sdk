import sys
import os
from src.sambanova.api_client import SambanovaAPIClient
from src.sambanova.translation import Translation

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def main() -> None:
    api_key = os.getenv("SN_API_KEY")
    if not api_key:
        raise ValueError("Missing SN_API_KEY environment variable")

    client = SambanovaAPIClient(api_key,
        "application/text",  )

    # Path to your audio file
    audio_file_path = "examples/testdata/translation/sample_audio3.mp3"  
    model_name = "Whisper-Large-v3"

    # Set the target language for translation here
    target_language = "english"  

    print(f"Audio File: {audio_file_path} \nTranslating audio to {target_language.title()} (plain text response)...\n")
    text_response = Translation.create(
        client,
        audio_file_path,   
        model_name,      
        language=target_language,
        response_format="text",
        stream=False
    )
    transcript = text_response if isinstance(text_response, str) else text_response.get("text", "")
    print("Translated Audio in text\n",transcript)

if __name__ == "__main__":
    main()