import requests


##################
# API call with query parameters

# q: The search query. In this case, we are searching for repositories related to "python api".
# sort: The field by which to sort the results. We are sorting by "stars" to get the most popular repositories.
# order: The order of the results. "desc" means descending order, so we will get the repositories with the most stars first.
params = {
    "q": "Gen AI Architecture in Python",
    "sort": "stars",
    "order": "desc"
}

search_url = "https://api.github.com/search/repositories"

search_response = requests.get(search_url, params = params)

print("Final URL : ", search_response.url) # This will show the final URL with query parameters
print("Status Code:", search_response.status_code)
data_json = search_response.json()

for item in data_json['items'][:5]: # Print the top 5 repositories
    print("Repository Name:", item['name'])
    print("Stars:", item['stargazers_count'])
    print("URL:", item['html_url'])
    print("-" * 40)