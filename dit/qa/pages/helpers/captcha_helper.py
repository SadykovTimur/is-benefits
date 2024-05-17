import requests


def resolve_captcha(path: str, url: str) -> str:
    with open(path, "rb") as f:
        image = f.read()

    response = requests.post(f'{url}/api/v1/solution', files={"image": image}, timeout=15)

    return response.json()["solution"]
