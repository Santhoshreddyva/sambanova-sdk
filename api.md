# Sambanova Python SDK API Reference

This document provides a comprehensive overview of every API endpoint and operation available in the Sambanova Python SDK, including parameters, headers, and request/response bodies.

---

## Authentication

All endpoints require an API key.  
**Header:**  
`Authorization: Bearer <your_api_key>`

---

## Chat

### Chat Completion

**Endpoint:**  
`POST /v1/chat/completions`

**Import:**
```python
from src.sambanova.chat import ChatCompletion
from src.sambanova.api_client import SambanovaAPIClient
```

**Method:**
```python
ChatCompletion.create(
    client: SambanovaAPIClient,
    messages: list,
    model: str,
    max_tokens: int = 2048,
    stream: bool = True,
    stop: list = None,
    process_prompt: bool = True,
    do_sample: bool = False,
    stream_options: dict = {"include_usage": True},
    **kwargs
) -> Iterator[dict]
```

**Parameters:**
- `client`: SambanovaAPIClient instance (required)
- `messages`: List of message dicts, e.g. `[{"role": "user", "content": "Hello"}]` (required)
- `model`: Model name (required)
- `max_tokens`: Maximum tokens to generate (default: 2048)
- `stream`: Whether to stream responses (default: True)
- `stop`: List of stop sequences (default: ["<|eot_id|>"])
- `process_prompt`: Whether to process the prompt (default: True)
- `do_sample`: Whether to sample (default: False)
- `stream_options`: Dict of stream options (default: {"include_usage": True})

**Headers:**
- `Authorization: Bearer <your_api_key>`
- `Content-Type: application/json`

**Request Body Example:**
```json
{
  "messages": [{"role": "user", "content": "Hello, how are you?"}],
  "model": "Llama-4-Maverick-17B-128E-Instruct",
  "max_tokens": 2048,
  "stream": true,
  "stream_options": {"include_usage": true},
  "stop": ["<|eot_id|>"],
  "process_prompt": true,
  "do_sample": false
}
```

**Response (streamed):**
Each chunk is a JSON dict, e.g.:
```json
{
  "choices": [
    {
      "delta": {"content": "Hello!"},
      "index": 0
    }
  ]
}
```

---

## Image

### Image Completion

**Endpoint:**  
`POST /v1/image/completions`

**Import:**
```python
from src.sambanova.image import Image
from src.sambanova.api_client import SambanovaAPIClient
```

**Method:**
```python
Image.create(
    client: SambanovaAPIClient,
    messages: list,
    model: str,
    max_tokens: int = 300,
    temperature: float = 0.7,
    stream: bool = False,
    **kwargs
) -> dict
```

**Parameters:**
- `client`: SambanovaAPIClient instance (required)
- `messages`: List of message dicts, including image data (required)
- `model`: Model name (required)
- `max_tokens`: Maximum tokens to generate (default: 300)
- `temperature`: Sampling temperature (default: 0.7)
- `stream`: Whether to stream responses (default: False)

**Headers:**
- `Authorization: Bearer <your_api_key>`
- `Content-Type: application/json`

**Request Body Example:**
```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "Describe this image."},
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,<base64_image>"}}
      ]
    }
  ],
  "model": "Llama-4-Maverick-17B-128E-Instruct",
  "max_tokens": 300,
  "temperature": 0.7,
  "stream": false
}
```

**Response:**
```json
{
  "choices": [
    {
      "message": {"role": "assistant", "content": "This image shows..."},
      "index": 0
    }
  ]
}
```

---

## Embeddings

### Embeddings

**Endpoint:**  
`POST /v1/embeddings`

**Import:**
```python
from src.sambanova.embeddings import Embeddings
from src.sambanova.api_client import SambanovaAPIClient
```

**Method:**
```python
Embeddings.create(
    client: SambanovaAPIClient,
    messages: list,
    model: str,
    **kwargs
) -> dict
```

**Parameters:**
- `client`: SambanovaAPIClient instance (required)
- `messages`: List of strings to embed (required)
- `model`: Model name (required)

**Headers:**
- `Authorization: Bearer <your_api_key>`
- `Content-Type: application/json`

**Request Body Example:**
```json
{
  "messages": [
    "Text 1 to embed.",
    "Text 2 to embed."
  ],
  "model": "E5-Mistral-7B-Instruct"
}
```

**Response:**
```json
{
  "embeddings": [
    [0.123, 0.456, ...],
    [0.789, 0.012, ...]
  ]
}
```

---

## Audio

### Audio Reasoning

**Endpoint:**  
`POST /v1/audio/reasoning`

**Import:**
```python
from src.sambanova.audio import Audio
from src.sambanova.api_client import SambanovaAPIClient
```

**Method:**
```python
Audio.create(
    client: SambanovaAPIClient,
    messages: list,
    model: str,
    max_tokens: int = 200,
    **kwargs
) -> dict
```

**Parameters:**
- `client`: SambanovaAPIClient instance (required)
- `messages`: List of message dicts, including audio content (required)
- `model`: Model name (required)
- `max_tokens`: Maximum tokens to generate (default: 200)

**Headers:**
- `Authorization: Bearer <your_api_key>`
- `Content-Type: application/json`

**Request Body Example:**
```json
{
  "messages": [
    {"role": "assistant", "content": "You are a helpful assistant."},
    {"role": "user", "content": [
      {"type": "audio_content", "audio_content": {"content": "data:audio/mp3;base64,<base64_audio>"}}
    ]},
    {"role": "user", "content": "What is in this audio?"}
  ],
  "model": "Qwen2-Audio-7B-Instruct",
  "max_tokens": 200
}
```

**Response:**
```json
{
  "choices": [
    {
      "message": {"role": "assistant", "content": "This audio contains..."},
      "index": 0
    }
  ]
}
```

---

## Transcription

### Transcribe Audio File

**Endpoint:**  
`POST /v1/audio/transcriptions`

**Import:**
```python
from src.sambanova.transcription import Transcription
from src.sambanova.api_client import SambanovaAPIClient
```

**Method:**
```python
Transcription.transcribe_audio_file(
    client: SambanovaAPIClient,
    model: str,
    audio_file_path: str,
    language: str = "english",
    response_format: str = "text",
    **kwargs
) -> dict
```

**Parameters:**
- `client`: SambanovaAPIClient instance (required)
- `model`: Model name (required)
- `audio_file_path`: Path to audio file (required)
- `language`: Language of audio (default: "english")
- `response_format`: Format of response (default: "text")

**Headers:**
- `Authorization: Bearer <your_api_key>`
- `Content-Type: multipart/form-data`

**Request Body Example:**  
Form-data with fields:
- `file`: (binary audio file)
- `model`: "Whisper-Large-v3"
- `language`: "english"
- `response_format`: "text"

**Response:**
```json
{
  "text": "Transcribed text here."
}
```

---

## Models

### List Available Models

**Endpoint:**  
`GET /v1/models`

**Import:**
```python
from src.sambanova.model_list import models
from src.sambanova.api_client import SambanovaAPIClient
```

**Method:**
```python
models.get_available_models(client: SambanovaAPIClient) -> list[dict]
```

**Parameters:**
- `client`: SambanovaAPIClient instance (required)

**Headers:**
- `Authorization: Bearer <your_api_key>`

**Response:**
```json
{
  "data": [
    {
      "id": "Llama-4-Maverick-17B-128E-Instruct",
      "status": "available",
      "context_length": 2048,
      ...
    }
  ]
}
```

---

### Get Model Details

**Endpoint:**  
`GET /v1/models/{model_id}`

**Method:**
```python
models.get_model_details(client: SambanovaAPIClient, model_id: str) -> dict
```

**Parameters:**
- `client`: SambanovaAPIClient instance (required)
- `model_id`: Model identifier (required)

**Headers:**
- `Authorization: Bearer <your_api_key>`

**Response:**
```json
{
  "id": "Llama-4-Maverick-17B-128E-Instruct",
  "status": "available",
  "context_length": 2048,
  ...
}
```

---

## Error Handling

All API methods may raise exceptions on network or API errors.  
Typical exceptions include `RuntimeError` for failed requests.

---

## Notes

- All methods require a valid `SambanovaAPIClient` instance.
- Most methods accept additional keyword arguments for advanced options.
- Streaming endpoints yield results as they arrive; non-streaming endpoints return a single dictionary.

---