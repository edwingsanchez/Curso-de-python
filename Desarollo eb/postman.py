import requests


def fetch(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    print(fetch("https://httpbin.org/get"))
