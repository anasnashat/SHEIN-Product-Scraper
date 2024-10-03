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

    # Create a DataFrame from the collected data
    new_data_df = pd.DataFrame(flattened_data_list)

    # Create directory if it doesn't exist
    os.makedirs('ScrapedData', exist_ok=True)

    # Path to the Excel file
    excel_file = f'ScrapedData/{file_name}.xlsx'

    # Append to the existing file or create a new one
    if os.path.exists(excel_file):
        # Load existing data
        existing_data_df = pd.read_excel(excel_file)

        # Append the new data
        combined_df = pd.concat([existing_data_df, new_data_df], ignore_index=True)
        combined_df.to_excel(excel_file, index=False)
        print(f"Data appended to {excel_file}")
    else:
        # Save new data
        new_data_df.to_excel(excel_file, index=False)
        print(f"Data saved to {excel_file}")
