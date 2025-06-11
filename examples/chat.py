import os
from src.sambanova.chat import SambanovaAPIClient, ChatCompletion

api_key = os.getenv("SN_API_KEY")
if not api_key:
    raise ValueError("Missing SN_API_KEY environment variable")

client = SambanovaAPIClient(api_key)
messages = []
MODEL_NAME = "Llama-4-Maverick-17B-128E-Instruct"
MAX_TOKENS = 4096  

# Show model name before chat
print(f"Model: {MODEL_NAME}")
print(f"Start chatting (max tokens: {MAX_TOKENS}, type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in {"exit", "quit"}:
        break

    messages.append({"role": "user", "content": user_input})

    stream = ChatCompletion.create(
        client,
        messages=messages,
        model=MODEL_NAME
    )

    response = ""
    usage = None
    for chunk in stream:
        choices = chunk.get("choices", [])
        if not choices:
            continue
        delta = choices[0].get("delta", {})
        content = delta.get("content", "")
        response += content
        # Capture usage if present
        if "usage" in chunk:
            usage = chunk["usage"]
    print(response)
    messages.append({"role": "assistant", "content": response})

    # Show tokens left and usage
    if usage:
        total_tokens = usage.get("total_tokens", 0)
        tokens_left = MAX_TOKENS - total_tokens
        print(f"[tokens left: {tokens_left}, usage: {usage}]")
