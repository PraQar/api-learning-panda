import requests


search_url = "https://api.github.com/search/repositories"



try:
    search_response = requests.get(url = search_url, params = {"q": "Gen AI Architecture in Python", "sort": "stars", "order": "desc"})

    search_response.raise_for_status() # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
    response_data_json = search_response.json()

    for item in response_data_json['items'][:5]: # Print the top 5 repositories
        print(item['name'], "-", item['html_url'])
    
except requests.exceptions.Timeout:
    print("The request timed out. Please try again later.") # good production rule
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
except ValueError:
    print("Error parsing JSON response. Please check the API response format.")
