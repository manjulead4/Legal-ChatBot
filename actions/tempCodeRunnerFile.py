import requests
from dotenv import load_dotenv
import os

# Ensure environment variables are loaded
load_dotenv()

def test_bird_api():
    # Define the API URL (replace with the actual endpoint)
    api_url = "https://api.bird.com/v1/resource"  # Replace with the correct endpoint

    # Load the API key from the .env file
    api_key = os.getenv("g.a000vAgQqEDRwQkauAErCZJW4G479jE-aaMuhhwcCbJtXPf0P7ZuyDd6AX4EQEqgMjPdhti4egACgYKAd4SARASFQHGX2MipedkkVbDrjMLB74vItmAiRoVAUF8yKpaWVg2FhjdC0dw_iEF8_7M0076")

    # Set headers with the API key
    headers = {"Authorization": f"Bearer {api_key}"}

    # Define query parameters (adjust as needed)
    params = {"query": "test query"}

    # Make the API request
    try:
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            print("API Response:", response.json())
        else:
            print(f"Error {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        print("Request Exception:", str(e))

if __name__ == "__main__":
    test_bird_api()