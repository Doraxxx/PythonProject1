import requests
import json
import time

while True:
    n = input('Введите название валюты: ')
    response = requests.get("https://blockchain.info/ru/ticker")
    d = json.loads(response.text)
    d2 = json.loads(json.dumps(d[n]))
    print(f"Стоимость покупки {n}: ")
    print(d2['buy'])
    time.sleep(5)












