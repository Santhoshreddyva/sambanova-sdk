import os
from src.sambanova.api_client import SambanovaAPIClient
from src.sambanova.model_list.models import get_available_models

def main():
    api_key = os.getenv("SN_API_KEY")
    if not api_key:
        raise ValueError("Missing SN_API_KEY environment variable")

    client = SambanovaAPIClient(api_key)
    try:
        models = get_available_models(client)
        if not models:
            print("No models found.")
            return
        print(f"{'Model Name':32} {'Context':8} {'Max Tokens':10} {'Prompt $':12} {'Completion $':12}")
        print("-" * 80)
        for model in models:
            name = model.get("id", "N/A")
            context_length = model.get("context_length", "N/A")
            max_tokens = model.get("max_completion_tokens", "N/A")
            pricing = model.get("pricing", {})
            prompt_price = pricing.get("prompt", "N/A")
            completion_price = pricing.get("completion", "N/A")
            print(f"{name:32} {str(context_length):8} {str(max_tokens):10} {prompt_price:12} {completion_price:12}")
    except Exception as e:
        print("Error fetching models:", e)

if __name__ == "__main__":
    main()
