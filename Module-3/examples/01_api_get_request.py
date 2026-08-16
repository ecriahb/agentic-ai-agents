import requests


def main():
    url = "https://httpbin.org/get"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    print("Status code:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("JSON body:")
    print(response.json())


if __name__ == "__main__":
    main()
