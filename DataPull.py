# http://localhost:5025/api/Categories/GetList

import requests
import pandas as pd

# Get the data from the API
def get_data(url):
    response = requests.get(url)
    return response.json()

# get_products_by_category_id_data buradan aldığım json verisini pandas dataframe'e çevirip csv olarak kaydedeceğim.
def get_products_by_category_id_data_to_csv(json_data):
    df = pd.DataFrame(json_data)
    df.to_csv('products.csv', index=False)


def get_products_by_category_id_data(id, is_deleted_datas):
    url = f"http://localhost:5025/api/Products/category/{id}?isDeleteShow={is_deleted_datas}"
    response = requests.get(url=url)
    get_products_by_category_id_data_to_csv(response.json()["data"])
    return response.json()
