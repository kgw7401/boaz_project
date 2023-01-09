from faker import Faker
import uuid
import random
import pandas as pd
import json

with open("shop.json", 'r') as f:
    shop = json.load(f)

shop_name = []
for i in shop['DATA']:
    shop_name.append(i['name_kor'])

data = pd.read_csv("menu.csv")
shop_id = list(set(data['식당ID'].to_list()))
menu_id = data.groupby('식당ID')['메뉴ID'].apply(list).reset_index()
menu_name = data.groupby('식당ID')['메뉴명'].apply(list).reset_index()
price = data.groupby('식당ID')['메뉴가격'].apply(list).reset_index()

print(menu_id)
menu_df = pd.merge(menu_id, menu_name)
print(menu_df)
# shop_info = []

# print(menu_name[menu_name['식당ID'] == 2858]['메뉴명'])

# for i in range(shop_name):
#     menus = [i for i in zip(menu_id)]
#     shop_info.append({
#         'shop_id': shop_id[i], 
#         'shop_name': shop_name[i], 
#         'delivery_time': random.randint(20, 60), 
#         'menus': })