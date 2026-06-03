import requests
from dotenv import load_dotenv
import os


load_dotenv() # Load environment variables from .env file


# get the API key from environment variable
api_key = os.getenv("API_KEY")

search_url = "https://api.github.com/user"

# Example of adding custom headers to the API request
headers = {
    "Authorization": f"Bearer {api_key}", # This is how you can include the API key in the Authorization header
    "Accept": "application/vnd.github.v3+json" # receive response in GitHub's v3 API format that is JSON
}

response = requests.get(url = search_url , headers = headers)

print("Status Code:", response.status_code) # 200 means success !!, 401 means unauthorized (invalid API key), 403 means forbidden (rate limit exceeded)
print("Response Headers:", response.headers)
print("Response Text:", response.text)