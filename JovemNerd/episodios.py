#%%
import requests
import datetime
import os
import json
import pandas as pd
import time

#%%
class Collector():
    def __init__(self, url, instance_name):
        self.url = url
        self.instance_name = instance_name

    def get_content(self,**kwargs):
        resp = requests.get(self.url, params=kwargs)
        return resp
    
    def save_parquet(self,data):
        base_dir = os.path.abspath(r"JovemNerd")
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
        parquet_dir = os.path.join(base_dir, f"data/{self.instance_name}/parquet")
        os.makedirs(parquet_dir, exist_ok=True)
        file_path = os.path.join(parquet_dir, f"{now}.parquet")
        
        print(f"Saving DataFrame to: {file_path}")
        
        df = pd.DataFrame(data)
        df.to_parquet(file_path, index=False)


    def save_json(self,data):
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.%f")
        base_dir = os.path.abspath(r"JovemNerd")
        
        json_dir = os.path.join(base_dir, f"data/{self.instance_name}/json")
        os.makedirs(json_dir, exist_ok=True)
        file_path = os.path.join(json_dir, f"{now}.json")
        print(f"Saving JSON data to: {file_path}") 
        with open(file_path, 'w') as open_file:
            json.dump(data, open_file, indent=4)
        print("JSON data saved successfully")
    
    def save_data(self,data, format='json'):
        if format=='json':
            self.save_json(data=data)
        elif format == 'parquet':
            self.save_parquet(data=data)
    
    def get_and_save(self,save_format='json', **kwargs):
        resp = self.get_content(**kwargs)
        if resp.status_code == 200:
            data = resp.json()
            self.save_data(resp.json(),save_format)
        else:
            data = None
            print(f"Request sem sucesso: {resp.status_code}")
        return data
    
    def auto_exec(self, save_format='json',date_stop='2000-01-01'):
        page=1
        while True:
            print(page)
            data = self.get_and_save(save_format='json'
                                     , page=page
                                     ,per_page=1000)
            if data == None:
                print("Erro ao coletar dados")
                datetime.time.sleep(60*5)
            else: 
                date_last = pd.to_datetime(data[-1]["published_at"]).date()
                if date_last < pd.to_datetime(date_stop).date():
                    print(f"Deu a Data: {date_stop}")
                    break
                elif len(data) < 1000:
                    print("Menos de 1000 itens")
                    break
                page+=1
                time.sleep(5)


# %%
url = "https://api.jovemnerd.com.br/wp-json/jovemnerd/v1/nerdcasts/"
collect = Collector(url=url, instance_name="episodios")
collect.auto_exec()
# %%
