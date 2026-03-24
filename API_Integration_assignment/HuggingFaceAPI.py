import os
import requests
from dotenv import load_dotenv

# get API key from .env file and initialize HuggingFace client
load_dotenv()

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}",
    "Content-Type": "application/json",
}

#function to query HuggingFace API with a prompt and get response
def query_api(user_prompt):
    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct:cerebras",
        "messages": [
            {"role": "user", "content": user_prompt}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

#main function to take user input and query the API
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying from HuggingFace API ..... ")
    result = query_api(user_prompt)

    # extract the text safely
    if "choices" in result and len(result["choices"]) > 0:
        print("Response:\n" + result["choices"][0]["message"]["content"])
    else:
        print("Unexpected response format:\n", result)