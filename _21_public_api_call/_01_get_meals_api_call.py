import requests


def get_random_meal(meal_name: str = "") -> dict:
    url = "https://api.freeapi.app/api/v1/public/meals"
    params = {
        "q": meal_name,
        "limit": 1
    }

    response = requests.get(url=url, params=params, timeout=10)
    print(response.raise_for_status())
    print("Response Code :: ", response.status_code)
    return response.json()


def parse_json_response(json_response: dict):
    for key, value in json_response.items():
        print(f"{key} :: {value}")


def main():
    meal = get_random_meal("Pasta")
    parse_json_response(meal)


if __name__ == "__main__":
    main()
