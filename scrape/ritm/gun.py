import requests
import json
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import urllib3

urllib3.disable_warnings()

start_date = datetime(2020, 1, 1)


end_date = datetime(2024, 3, 5)


print((datetime.now() - start_date + timedelta(days=2)).days)

res = requests.get('https://www.ritm.gov.tr/amline/data_file_ritm_03032024.txt', verify=False)
data = res.text

rows = data.split('\n')

kurulu_guc = rows[0]

rows = rows[1:len(rows)-1]

tarih = []
kurulu_guc = []
tahmin = []
uretim = []
Q5 = []
Q25 = []
Q75 = []
Q95 = []
tahmin = []
uretim = []


for i in rows:
    parsed = i.split(',')

    tarih.append(parsed[0])
    Q5.append(parsed[1])
    Q25.append(parsed[2])
    Q75.append(parsed[3])
    Q95.append(parsed[4])
    tahmin.append(parsed[5])
    try:
        uretim.append(parsed[6])
    except IndexError:
        uretim.append(np.nan)


print(kurulu_guc)

df = pd.DataFrame({    
    'tarih': tarih,
    'tahmin': tahmin,
    'uretim': uretim,
    'Q5': Q5,
    'Q25': Q25,
    'Q75': Q75,
    'Q95': Q95
})

print(df)
