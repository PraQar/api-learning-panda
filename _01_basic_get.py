import requests

# Head over to link to know all the response code with their meaning : 
# # url https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

url = "https://api.github.com"
response = requests.get(url)

print("Status Code:", response.status_code) #200 - means success !!
# print("Headers:", response.headers)
# print("Text:", response.text)

# This will parse the JSON response and print it as a Python dictionary
response_data = response.json()
print("JSON:", type(response_data))

# Print the keys of the JSON response
print("Keys in JSON response:", response_data.keys())