import os
import cohere
from dotenv import load_dotenv

# get API key from .env file and initialize Cohere client
load_dotenv()
client = cohere.Client(os.getenv("COHERE_API_KEY"))

#function to query cohere api with a prompt with its model
def query_api(prompt):
    try:
        response = client.chat(
            message=prompt,
            model="command-a-03-2025" 
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

#main function to take user input and query the API
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:\n", result)