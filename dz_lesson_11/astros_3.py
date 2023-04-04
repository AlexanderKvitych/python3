# Вивезти всіх космонавтів(кількість і імена) http://api.open-notify.org/astros.json
import requests

my_list = []
astros = requests.get('http://api.open-notify.org/astros.json')
for obj in astros.json()['people']:
    # print(obj)
    if obj in astros.json()['people'] and obj not in my_list:
        my_list.append(obj['name'])
        # print(my_list, len(my_list))
print(f'Список космонавтів: {my_list}\nКількість космонавтів: {len(my_list)}')