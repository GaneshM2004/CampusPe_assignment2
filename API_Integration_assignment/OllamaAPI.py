import requests
import json

#function to query Ollama API with a prompt and get response
def query_api(prompt):
    url = "http://localhost:11434/api/generate" #localhost URL for Ollama API
    payload = {
        #using this model for ollama api which was downloaded and added to ollama
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

#main function to take user input and query the API
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:\n" + result)