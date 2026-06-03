import requests

# POST = Send data to the API to create a new resource. 
# The server processes the data and returns a response, often including the newly created resource or a confirmation message.
post_url = "https://jsonplaceholder.typicode.com/posts"

# Data to be sent in the POST request
payload = {
    "title": "Learning API calls with Python",
    "body": "This is a sample post request to demonstrate how to send data to an API endpoint using Python's requests library.",
    "userId": 1
}

headers = {
    "Content-Type": "application/json" # This header tells the server that we are sending JSON data in the request body
}
response = requests.post(url = post_url, json = payload, headers = headers, timeout = 10) # timeout is optional but good practice to avoid hanging requests

print("Status Code:", response.status_code) # 201 means created successfully
print("POST Url : ", response.url) # This will show the URL to which the POST request was sent
print("Response JSON:", response.json()) # This will show the response from the server, 
# which should include the data we sent along with an ID for the new post created by the API.