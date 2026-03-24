import os
from groq import Groq
from dotenv import load_dotenv

# get API key from .env file and initialize Groq client
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#function to query Groq API with a prompt of its model and get response
def query_api(prompt):
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            #using this model for groq api
            model="llama-3.1-8b-instant",
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

#main function to take user input and query the API
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying from Groq API ..... ")
    result = query_api(user_prompt)
    print("Response:\n" + result)