import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import urllib3

urllib3.disable_warnings()

start_date = datetime(2024, 3, 2)

end_date = datetime(2024, 3, 6)

days = ((end_date - start_date).days + 1)

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

last=0

while start_date <= end_date:
    url_ex = start_date.strftime('_%d%m%Y')
    if start_date.strftime('_%d%m%Y') == datetime.now().strftime('_%d%m%Y'):
        url_ex = ''
        last=1
    res = requests.get(f'https://www.ritm.gov.tr/amline/data_file_ritm{url_ex}.txt', verify=False)
    print(res.url)
    data = res.text
    
    if start_date + timedelta(days=2) > end_date and start_date != end_date: #1 gun sonra son gun ise
        start_date += timedelta(days=1)
    else:
        start_date += timedelta(days=2)
        
    rows = data.split('\n')

    kurulu_guc = rows[0]

    rows = rows[1:len(rows)-1]

    
    for i in rows:
        parsed = i.split(',')
        print(parsed)
        if(last==0):
            try:
                ctr = parsed[6]
            except IndexError:
                continue
        
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

df.to_csv('gun.csv', index=False)