import requests
import time

import pandas as pd


data = pd.read_csv("data/data_for_requests.csv", index_col='flat_id')

for flat_id, row in data.iterrows():
    params = {
        "user_id": str(flat_id),
        'params_model': row.to_dict()
    }
    response = requests.post('http://localhost:4555/', json=params)
    time.sleep(1)


