import requests
import json

API_KEY = '74b15c07c4094b7aaa345764a1dbc596'

longitude = 52.6584  # долгота
latitude  = 58.1394  # широта

prognoz_temperatury = []

api_response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=minutely,hourly,alerts&appid={API_KEY}&units=metric").text
json_response = json.loads(api_response)
for i in range(5):    
    prognoz_temperatury.append(json_response["daily"][i]["temp"]["morn"])
    

print("Средняя прогнозная утренняя температура в Глазове за пять дней, включая 24.02.2021, равна:", sum(prognoz_temperatury) / 5,
    "\nМаксимальная прогнозная утренняя температура в тот же период равна:", max(prognoz_temperatury))

    