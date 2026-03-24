import os
import google.generativeai as genai
from dotenv import load_dotenv

# get API key from .env file and initialize Gemini client
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# initialize the Gemini model
#using this model for gemini api and it is free tier model
model = genai.GenerativeModel('gemini-2.5-flash')

#function to query Gemini API with a prompt and get response
def query_api(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

#main function to take user input and query the API
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:\n" + result)