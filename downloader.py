import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def download_subscription(url):
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=30
        )

        response.raise_for_status()

        return response.text

    except Exception as e:
        print(f"خطا در دانلود:\n{url}")
        print(e)
        return None