import os
from sambanova.api_client import SambanovaAPIClient
from sambanova.embeddings import Embeddings

api_key = os.getenv("SN_API_KEY")
if not api_key:
    raise ValueError("Missing SN_API_KEY environment variable")

client = SambanovaAPIClient(api_key)
messages = [
    "Our solar system orbits the Milky Way galaxy at about 515,000 mph", 
    "Jupiter's Great Red Spot is a storm that has been raging for at least 350 years."
  ]

response = Embeddings.create(
    client,
    messages=messages,
    model="E5-Mistral-7B-Instruct"
)

# Handle the response appropriately
if "data" in response:
    embeddings = response["data"]
    for i, embedding in enumerate(embeddings):
        print(f"Embedding for message {i}: {embedding}")
else:
    print("Unexpected response format:", response)

