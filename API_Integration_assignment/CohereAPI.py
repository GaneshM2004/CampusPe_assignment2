import os
import cohere
from dotenv import load_dotenv

load_dotenv()
client = cohere.Client(os.getenv("COHERE_API_KEY"))

def query_api(prompt):
    try:
        response = client.chat(
            message=prompt,
            model="command-a-03-2025" 
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:\n", result)