import requests
from datetime import datetime
from pprint import pprint 
import csv 

city = 'Delhi'
api_key = ''

api_link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


req = requests.get(api_link)

# print(req.json()['weather'][0]['main'])
# print(req.json()['main']['temp'])


# curr_date = datetime.date().

# print(curr_date)


with open(file='weather_log.csv' , mode='r' , encoding='utf-8') as f :
            csvreader = list(csv.DictReader(f))
            pprint(csvreader)
           

