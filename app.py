from _06_api_client_module.api_client import APIClient

client = APIClient("https://api.github.com")

data = client.get("/search/repositories", params={
    "q": "python requests",
    "sort": "stars",
    "order":"desc"
})

for repo in data["items"][:5]:
    print(repo["name"], repo["html_url"])