import requests
import json

number = input('Enter your number : ')

url = f'http://127.0.0.1:5000/phone?number={number}'

res = requests.get(url)
data = res.text
data = json.loads(data)
for key, value in data.items():
    print(f"{key} : {value}")
