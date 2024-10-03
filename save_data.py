import os

import pandas as pd


def save(file_name: str, products: list):
    BASE_URL_TEMPLATE = 'https://ar.shein.com/SHEIN-{}-p-{}.html?src_module=All&src_identifier=on=PRODUCT_ITEMS_COMPONENT`cn=PRODUCT_ITEMS_COMPONENT_1`hz=0`ps=7_1_0`jc=itemPicking_003200800&src_tab_page_id=page_home1727898964238&mallCode=1'
    flattened_data_list = []

    for productData in products:
        goods_id = productData['goods_id']
        goods_url_name = productData.get("goods_url_name", "")
        product_image = productData.get("goods_img", "")

        # Constructing the product URL
        formatted_url_name = goods_url_name.replace(" ", "-")
        product_url = BASE_URL_TEMPLATE.format(formatted_url_name, goods_id)
        try:
            flattened_data = {
                "goods_id": goods_id,
                "goods_sn": productData["goods_sn"],  # SKU
                "mall_code": productData["mall_code"],
                "score": productData["score"],
                "goods_name": productData["goods_name"],
                "retail_price_amount": productData["retailPrice"]["amount"],
                "retail_price_usd": productData["retailPrice"]["usdAmount"],
                "sale_price_amount": productData["salePrice"]["amount"],
                "sale_price_usd": productData["salePrice"]["usdAmount"],
                "store_code": productData["storeInfo"]["storeCode"],
                "store_title": productData["storeInfo"]["title"],
                "store_logo": productData["storeInfo"]["logo"],
                "product_image": product_image,  # Adding product image URL
                "product_url": product_url  # Adding product URL
            }
            flattened_data_list.append(flattened_data)
        except Exception as e:
            print(f"An error occurred: {e}")

    # Create a DataFrame from the collected data
    df = pd.DataFrame(flattened_data_list)

    # Save to Excel
    try:
        os.mkdir('ScrapedData')
        excel_file = f'ScrapedData/{file_name}.xlsx'
    except Exception as e:
        excel_file = f'ScrapedData/{file_name}.xlsx'

    df.to_excel(excel_file, index=False)

    print(f"Data saved to {excel_file}")
