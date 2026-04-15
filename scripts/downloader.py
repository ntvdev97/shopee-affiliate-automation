import requests

def download_video(url, path):
    r = requests.get(url)
    with open(path, "wb") as f:
        f.write(r.content)