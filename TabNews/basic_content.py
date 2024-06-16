# %%
import requests
import pandas as pd
import datetime
import json
import os
import time

#%%
def get_response(**kwargs):
    url_base = "https://www.tabnews.com.br/api/v1/contents"
    resp = requests.get(url=url_base, params=kwargs)
    return resp

def save_data(data, option='json'):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
    base_dir = os.path.abspath(r"TabNews")
    
    try:
        if option == 'json':
            json_dir = os.path.join(base_dir, "contents/json")
            os.makedirs(json_dir, exist_ok=True)
            file_path = os.path.join(json_dir, f"{now}.json")
            print(f"Saving JSON data to: {file_path}") 
            with open(file_path, 'w') as open_file:
                json.dump(data, open_file, indent=4)
            print("JSON data saved successfully")

        elif option == 'dataframe':
            # Ensure Parquet directory exists
            parquet_dir = os.path.join(base_dir, "contents/parquet")
            os.makedirs(parquet_dir, exist_ok=True)
            file_path = os.path.join(parquet_dir, f"{now}.parquet")
            print(f"Saving DataFrame to: {file_path}")
            df = pd.DataFrame(data)
            df.to_parquet(file_path, index=False)
            print("DataFrame saved successfully")
    except Exception as e:
        print(f"An error occurred while saving data: {e}")

# Request data and save
#%%
page = 1
while True:
    print(page)
    resp = get_response(page=page, per_page=100, strategy="new")
    if resp.status_code == 200:
        data = resp.json()
        save_data(data=data)

        if len(data) < 100:
            break
        page += 1
        time.sleep(2)
    else:
        print(resp.status_code)
        print(resp.json())
        time.sleep(30)
# %%
