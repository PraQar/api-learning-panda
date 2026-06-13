import requests
import json
from dotenv import load_dotenv
import os


def get_headers(token: str) -> dict:
    return {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}"
    }


# call the api and handle errors
def call_api(url: str, headers: dict, params: dict | None = None):
    try:
        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        raise RuntimeError("Request timed out")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"An error occurred: {e}")
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"HTTP error occurred: {e}")


def inspect_json(data, level=0):
    indent = " " * level
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{indent}{key}: {type(value).__name__}")

            if isinstance(value, (dict, list)):
                inspect_json(value, level + 1)

    elif isinstance(data, list):
        print(f"{indent} List of {len(data)} items")

        if len(data) > 0:
            print(f"{indent}First Item Structure : ")
            inspect_json(data[0], level + 1)


def extract_repo_summary(repo: dict) -> dict:
    return {
        "name": repo.get("name"),
        "full_name": repo.get("full_name"),
        "private": repo.get("private"),
        "owner": repo.get("owner", {}).get("login"),
        "html_url": repo.get("html_url"),
        "description": repo.get("description"),
        "created_at": repo.get("created_at"),
        "updated_at": repo.get("updated_at"),
        "pushed_at": repo.get("pushed_at"),
        "stargazers_count": repo.get("stargazers_count"),
        "watchers_count": repo.get("watchers_count"),
        "language": repo.get("language"),
        "forks_count": repo.get("forks_count"),
        "open_issues_count": repo.get("open_issues_count")
    }


def main():

    load_dotenv()

    token = os.getenv("GITHUB_TOKEN_KEY")

    if not token:
        raise RuntimeError("GitHub token not found in environment variables.")

    headers = get_headers(token)

    user_url = "https://api.github.com/user"
    repos_url = "https://api.github.com/user/repos"

    print("\nCalling authenticated user API...")

    user = call_api(user_url, headers)

    print("\nAuthenticated User Info:")
    print("username: ", user.get("login"))
    print("name: ", user.get("name"))
    print("email: ", user.get("email"))
    print("User_url : ", user.get("html_url"))

    print("\n Calling repositories API...")
    repos = call_api(
        repos_url,
        headers,
        params={
            "per_page": 5,
            "sort": "updated"
        }
    )
    print("\n JSON Strucutre of Repositories Response:")
    inspect_json(repos)

    repo_summaries = [extract_repo_summary(repo) for repo in repos]

    print("\n Repository Summaries:")
    print("\n{'Name':30} {'Private':10} {'Language':15} {'Stars':5}")
    print("-" * 80)

    for repo in repo_summaries:
        print(
            f"{str(repo['name'])[:30]:30} "
            f"{str(repo['private']):10} "
            f"{str(repo['language']):15} "
            f"{str(repo['stargazers_count']):5}"
        )

    print("\n End of API calls and data extraction.")
    print(json.dumps(repo_summaries, indent=4))


if __name__ == "__main__":
    main()
