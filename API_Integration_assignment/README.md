# AI API Integration Assignment

## Assignment Description
This Assignment demonstrates how to integrate and work with 5 different Generative AI APIs using Python. It includes individual programs capable of sending user prompts to Groq, Ollama, Hugging Face, Google Gemini, and Cohere. 

## Setup Instructions
1. Clone this repository to your local machine.
2. Ensure Python is installed.
3. Install the required dependencies by running:
   `pip install -r requirements.txt`
4. Make sure Ollama is downloaded, installed, and actively running on your local machine.

## Obtaining API Keys
* **OpenAI:** Sign up at https://platform.openai.com/ and generate a key under API Keys.
* **Groq:** Sign up at https://console.groq.com/ and generate a key.
* **Ollama:** No API key is required, but you must install Ollama from https://ollama.ai/ and pull a model (e.g., `ollama run llama3`).
* **Hugging Face:** Sign up at https://huggingface.co/ and generate an Access Token in settings and use free serverless inference model.
* **Google Gemini:** Get a key from Google AI Studio at https://makersuite.google.com/app/apikey.
* **Cohere:** Sign up at https://dashboard.cohere.com/ and navigate to API Keys.

## Setting Environment Variables
To keep your credentials secure, set the following environment variables on your system:
* `OPENAI_API_KEY`
* `GROQ_API_KEY`
* `HUGGINGFACE_API_KEY`
* `GOOGLE_API_KEY`
* `COHERE_API_KEY`

By using .env file where these environment variables are declared
So that .env file doesnt get pushed to github, We use gitignore.


## How to Run
Execute each program via the terminal. For example:
`python GeminiAPI.py`

You will be prompted to enter a string, and the output of the console will output the API response.
