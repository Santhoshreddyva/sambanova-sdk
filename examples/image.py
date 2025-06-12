from pathlib import Path
import os
import base64
import json
from sambanova.api_client import SambanovaAPIClient
from sambanova.image import Image 

def main() -> None:
    api_key = os.getenv("SN_API_KEY")
    if not api_key:
        raise ValueError("Missing SN_API_KEY environment variable")

    client = SambanovaAPIClient(api_key)

    # Path to your image file
    image_path = Path("examples/testdata/image/sample_image.jpg")
    if not image_path.is_file():
        print(f"Error: Image file not found at {image_path}")
        return

    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is happening in this image?"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ]

    response = Image.create(
        client,
        messages=messages,
        model="Llama-4-Maverick-17B-128E-Instruct",
        max_tokens=300,
        temperature=0.7,
        top_p=0.9,
        top_k=50,
        stream=False 
    )

    # Print only the response content
    if isinstance(response, dict) and "choices" in response:
        for choice in response["choices"]:
            if "message" in choice and "content" in choice["message"]:
                print("Response:", choice["message"]["content"])
            else:
                print("Response:", choice)
    else:
        print("Response:", response)

if __name__ == "__main__":
    main()
