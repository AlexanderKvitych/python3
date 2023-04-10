'''
Write a script that reads the data from previous CSV file and creates a new file called high_scores.csv where each row contains the player name and their highest score. Final score should sorted by descending of highest score

The output CSV file should look like this:

Player name, Highest score
Kate, 907
Mary, 897
Luke, 784
Mark, 725
Josh, 345
...
'''
import pandas as pd
df = pd.read_csv('dz_lesson_12/txt_file/player_game.csv') # Відкриваємо файл який створили
df.rename(columns = {'Score':'Highest score'}, inplace = True ) # Робимо зміну столбця
sorted_df = df.sort_values(by=["Highest score"], ascending = False) # Сортування 
sorted_df.to_csv('dz_lesson_12/txt_file/high_scores.csv') # Створюємо вже відсортований файл
print(sorted_df) 

file_open = pd.read_csv('dz_lesson_12/txt_file/sorted_player_game.csv') # Перегляд результату

'''
OUT: 
 Player name  Highest score
3      Victor            761
4      Marina            502
2         Den            483
1        Alex            274
0        Ivan            229
'''