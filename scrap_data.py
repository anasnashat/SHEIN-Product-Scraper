import requests


def fetch_data() -> list:
    all_products = []

    URL = 'https://ar.shein.com/api/ccc/productList/get?_ver=1.1.8&_lang=ar'
    CATE_ID = "003200800"
    LIMIT = 1000

    data = {
        "cateType": "itemPicking",
        "cateId": CATE_ID,
        "page": 1,
        "mallCodes": "",
        "limit": LIMIT,
        "adp": "",
        "scene": "home",
        "componentId": 39491512,
        "styleType": "VERTICAL_ITEMS",
        "channelName": "All",
        "blockKey": ""
    }

    response = requests.post(URL, data=data)
    if response.status_code == 200:
        products = response.json().get('data', {}).get('products', [])
        all_products.extend(products)
        print(f'Done adding all products from trend page ')
    else:
        print(f'Failed to retrieve data from page, status code: {response.status_code}')

    return all_products
