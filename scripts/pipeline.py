import os
import yaml

from crawl_shopee import get_hot_products
from crawl_tiktok import search_videos
from downloader import download_video
from editor import edit_video

def load_config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)

def run():
    config = load_config()

    products = get_hot_products(
        config["shopee"]["category_id"],
        config["shopee"]["limit"]
    )

    os.makedirs("videos/raw", exist_ok=True)
    os.makedirs("videos/edited", exist_ok=True)

    for p in products:
        videos = search_videos(p["name"], config["tiktok"]["max_videos"])

        for i, v in enumerate(videos):
            raw_path = f"videos/raw/{p['name']}_{i}.mp4"
            out_path = f"videos/edited/{p['name']}_{i}.mp4"

            print(f"Downloading {v}")
            download_video(v, raw_path)

            print(f"Editing {raw_path}")
            edit_video(raw_path, out_path, config["video"]["watermark_text"])

if __name__ == "__main__":
    run()