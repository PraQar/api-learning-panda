import requests

# APIClient is a small wrapper around the requests library.
# It simplifies making GET and POST calls by handling URL construction,
# timeout configuration, JSON parsing, and common request errors.
class APIClient:
    def __init__(self, base_url: str, timeout: int = 10):
        # Store the base URL for all API requests.
        # rstrip('/') removes any trailing slash so endpoint joining is consistent.
        self.base_url = base_url.rstrip("/")
        # Store the timeout value used for each request.
        self.timeout = timeout

    def get(self, endpoint: str, params: dict | None = None, headers: dict | None = None):
        # Build the full URL for the GET request.
        # lstrip('/') removes a leading slash from the endpoint to avoid double slashes.
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            # Send a GET request with optional query parameters and headers.
            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=self.timeout
            )
            # Raise an exception for HTTP 4xx/5xx responses.
            response.raise_for_status()
            # Parse the response body as JSON and return it.
            return response.json()

        except requests.exceptions.Timeout:
            # Handle request timeout separately.
            raise RuntimeError("The API request timed out.")

        except requests.exceptions.HTTPError as error:
            # Convert HTTP status errors into a runtime error with details.
            raise RuntimeError(f"HTTP error occurred: {error}")

        except requests.exceptions.RequestException as error:
            # Catch any other requests-related error.
            raise RuntimeError(f"API request failed: {error}")

        except ValueError:
            # Handle the case where the response cannot be decoded as JSON.
            raise RuntimeError("API response was not valid JSON.")

    def post(self, endpoint: str, payload: dict, headers: dict | None = None):
        # Build the full URL for the POST request.
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        try:
            # Send a POST request with the provided payload serialized as JSON.
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=self.timeout
            )
            # Raise an exception for any unsuccessful HTTP status code.
            response.raise_for_status()
            # Parse and return the JSON response body.
            return response.json()

        except requests.exceptions.Timeout:
            raise RuntimeError("The API request timed out.")

        except requests.exceptions.HTTPError as error:
            raise RuntimeError(f"HTTP error occurred: {error}")

        except requests.exceptions.RequestException as error:
            raise RuntimeError(f"API request failed: {error}")

        except ValueError:
            raise RuntimeError("API response was not valid JSON.")
