# Модуль hello
from hello import hello_name

name_user = input('Enter your name: ')
action = hello_name(name_user)
print(f' Hello {action} !')
