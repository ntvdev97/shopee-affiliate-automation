import requests

def search_videos(keyword, max_videos):
    url = f"https://www.tikwm.com/api/feed/search?keywords={keyword}"
    res = requests.get(url)
    data = res.json()

    videos = []
    for v in data["data"][:max_videos]:
        videos.append(v["play"])

    return videos