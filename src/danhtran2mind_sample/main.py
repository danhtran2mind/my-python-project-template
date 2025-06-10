import requests

def fetch_google_homepage() -> str:
    url = "https://google.com"
    headers = {
        'User-Agent': 'My Python Script/1.0'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.content
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

# Add the MyClass definition here
class MyClass:
    def __init__(self, name: str="sample_name") -> None:
        self.name = name
        print(f"MyClass instance created with name: {self.name}")

    def greet(self):
        print(f"Hello from {self.name}!")


if __name__ == "__main__":
    content = fetch_google_homepage()
    if content is not None:
        # You can save it to a file or process it further
        print(content[:100])  # Print the first 100 bytes for demonstration
