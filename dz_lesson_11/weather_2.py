# Взяти API-weather, розпарсити і вивезти погоду від користувача(вводить локацію, по цій локації повернеться погода, вологість і тд) https://openweathermap.org *Потрібна реєстрація і створення свого api-ключа

import requests
location = input('Enter: ')
appid = 'ddfddc911bfcbd893108f6ff33f556d6'

def information_base_information(location, appid):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/find", params={'q': location, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
            for d in data['list']]
        print("city:", cities)
        city_id = data['list'][0]['id']
        print('city_id=', city_id)
    except Exception as e:
        print("Error:", e)
    def information_current_weather(appid, city_id):
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            print("Умови:", data['weather'][0]['description'])
            print("Температура:", data['main']['temp'])
            print("Температура-мін:", data['main']['temp_min'])
            print("Температура-мах:", data['main']['temp_max'])
        except Exception as e:
            print("Error:", e)
    information_current_weather(appid, city_id)       
information_base_information(location, appid)