import requests
import json

def query_api(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "llama2",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:\n" + result)