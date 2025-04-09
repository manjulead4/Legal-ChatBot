import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

def test_gemini_api():
    # Load API key from .env
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not found in environment variables.")

    # API URL
    api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"

    # Prepare the request payload (adjust to the API's expected structure)
    data = {
        "prompt": {
            "text": "Say something inspiring!"
        }
    }

    try:
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            print("Gemini Response:", response.json())
        else:
            print(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print("Request Exception:", str(e))

if __name__ == "__main__":
    test_gemini_api()