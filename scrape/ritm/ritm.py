import requests
import json 
from datetime import datetime, timedelta
import urllib3

urllib3.disable_warnings()

# Define start and end dates
start_date = datetime(2022, 3, 1)
end_date = datetime(2022, 3, 10)
 
# Initialize an empty list
date_list = []
 
# Loop through the range of dates and append to the list
while start_date <= end_date:
    
    
    start_date += timedelta(days=1)
 
# Print the list of dates
print(date_list[0].strftime('%d%m%Y'))


res = requests.get('https://www.ritm.gov.tr/amline/data_file_ritm_29022024.txt', verify=False)
print(res.text)


