'''
Write a program that will simulate user score in a game. Create a list with 5 player's names. After that simulate 100 games for each player. As a result of the game create a list with player's name and his score (0-1000 range). And save it to a CSV file. File should looks like this:

Player name, Score
Josh, 56
Luke, 784
Kate, 90
Mark, 125
Mary, 877
Josh, 345
...
'''
import random
from random import randint
import csv
with open('dz_lesson_12/txt_file/player_game.csv', 'w') as file:
    file_name = ['Player name', 'Score']
    score_number = []
    writer = csv.DictWriter(file, fieldnames=file_name)
    for obj in range(1,6):
        if obj not in score_number:
            score_number.append(randint(1,1000))
    writer.writeheader()
    writer.writerow({'Player name': 'Ivan', 'Score': score_number[0]})
    writer.writerow({'Player name': 'Alex', 'Score': score_number[1]})
    writer.writerow({'Player name': 'Den', 'Score': score_number[2]})
    writer.writerow({'Player name': 'Victor', 'Score': score_number[3]})
    writer.writerow({'Player name': 'Marina', 'Score': score_number[4]})

with open('dz_lesson_12/txt_file/player_game.csv', 'r') as file_1:
    print(file_1.read())

'''
OUT: 
Player name,Score
Ivan,778
Alex,619
Den,133
Victor,131
Marina,681
'''