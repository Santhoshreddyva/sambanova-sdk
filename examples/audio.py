from pathlib import Path
import os
import base64
from sambanova.api_client import SambanovaAPIClient
from sambanova.audio import Audio

def main() -> None:
    api_key = os.getenv("SN_API_KEY")
    if not api_key:
        raise ValueError("Missing SN_API_KEY environment variable")

    client = SambanovaAPIClient(api_key)

    # Path to your audio file
    audio_file_path = (Path(__file__).parent / "testdata/audio/sample_audio.mp3").resolve()
    with open(audio_file_path, "rb") as audio_file:
        base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')

    # Prepare messages for audio reasoning (transcription/Q&A)
    messages = [
        {"role": "assistant", "content": "You are a helpful assistant."},
        {"role": "user", "content": [
            {
                "type": "audio_content",
                "audio_content": {
                    "content": f"data:audio/mp3;base64,{base64_audio}"
                }
            }
        ]},
        {"role": "user", "content": "What is in this audio?"}
    ]

    response = Audio.create(
        client,
        messages=messages,
        model="Qwen2-Audio-7B-Instruct",
        max_tokens= 200,
    )

        # Handle streaming or non-streaming response
    if isinstance(response, str) and response.startswith("data:"):
        import json
        full_response = ""
        for line in response.splitlines():
            if line.startswith("data:"):
                data_str = line[len("data:"):].strip()
                if not data_str or data_str in ("[DONE]",):
                    continue
                try:
                    data_json = json.loads(data_str)
                    content = data_json.get("choices", [{}])[0].get("delta", {}).get("content", "")
                    full_response += content
                except Exception as e:
                    print("Could not parse chunk as JSON:", e, "| Raw chunk:", repr(data_str))
        print("assistant:", full_response.strip())
    else:
        print("Response:", response)

if __name__ == "__main__":
    main()