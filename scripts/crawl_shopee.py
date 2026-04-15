import requests

def get_hot_products(category_id, limit):
    url = "https://shopee.vn/api/v4/search/search_items"

    params = {
        "by": "pop",
        "limit": limit,
        "match_id": category_id,
        "newest": 0,
        "order": "desc"
    }

    headers = {"user-agent": "Mozilla/5.0"}

    res = requests.get(url, params=params, headers=headers)
    data = res.json()

    products = []
    for item in data["items"]:
        products.append({
            "name": item["item_basic"]["name"]
        })

    return products