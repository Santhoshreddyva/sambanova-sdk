# Sambanova Python SDK

A Python SDK for interacting with Sambanova's REST APIs, including chat, image, audio, transcription, translation, and embeddings.

## Installation

```bash
pip install .
```

## Usage

### Chat Completion

```python
from src.sambanova.api_client import SambanovaAPIClient
from src.sambanova.chat import ChatCompletion

client = SambanovaAPIClient("your_api_key")
messages = [{"role": "user", "content": "Hello, how are you?"}]
stream = ChatCompletion.create(
    client,
    messages=messages,
    model="Llama-4-Maverick-17B-128E-Instruct"
)
response = ""
for chunk in stream:
    choices = chunk.get("choices", [])
    if not choices:
        continue
    delta = choices[0].get("delta", {})
    content = delta.get("content", "")
    response += content
print("Assistant:", response)
```

### Image Completion

```python
from src.sambanova.api_client import SambanovaAPIClient
from src.sambanova.image import Image
import base64

client = SambanovaAPIClient("your_api_key")
with open("path/to/image.jpg", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode('utf-8')
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Describe this image."},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
        ]
    }
]
response = Image.create(
    client,
    messages=messages,
    model="Llama-4-Maverick-17B-128E-Instruct",
    max_tokens=300,
    temperature=0.7,
    stream=False
)
print(response)
```

### Embeddings

```python
from src.sambanova.api_client import SambanovaAPIClient
from src.sambanova.embeddings import Embeddings

client = SambanovaAPIClient("your_api_key")
messages = [
    "Our solar system orbits the Milky Way galaxy at about 515,000 mph",
    "Jupiter's Great Red Spot is a storm that has been raging for at least 350 years."
]
response = Embeddings.create(
    client,
    messages=messages,
    model="E5-Mistral-7B-Instruct"
)
print(response)
```

### Audio Reasoning

```python
from src.sambanova.api_client import SambanovaAPIClient
from src.sambanova.audio import Audio
import base64

client = SambanovaAPIClient("your_api_key")
with open("path/to/audio.mp3", "rb") as audio_file:
    base64_audio = base64.b64encode(audio_file.read()).decode('utf-8')
messages = [
    {"role": "assistant", "content": "You are a helpful assistant."},
    {"role": "user", "content": [
        {"type": "audio_content", "audio_content": {"content": f"data:audio/mp3;base64,{base64_audio}"}}
    ]},
    {"role": "user", "content": "What is in this audio?"}
]
response = Audio.create(
    client,
    messages=messages,
    model="Qwen2-Audio-7B-Instruct",
    max_tokens=200,
)
print(response)
```

### Transcription

```python
from src.sambanova.api_client import SambanovaAPIClient
from src.sambanova.transcription import Transcription

client = SambanovaAPIClient("your_api_key")
audio_file_path = "path/to/audio.mp3"
response = Transcription.transcribe_audio_file(
    client,
    model="Whisper-Large-v3",
    audio_file_path=audio_file_path,
    language="english",
    response_format="text