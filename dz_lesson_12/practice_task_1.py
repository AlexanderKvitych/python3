# Create file with some content. As example you can take this one

import shutil
with open('dz_lesson_12/txt_file/poem.txt', 'w') as file:
    file.write('''
    Тому що ніколи тебе не вирвеш,
    ніколи не забереш,
    тому що вся твоя свобода
    складається з меж,
    тому що в тебе немає
    жодного вантажу,
    тому що ти ніколи не слухаєш,
    оскільки знаєш і так,
    що я скажу,
    ''')
# Create second file and copy content of the first file to the second file in upper case.
# copy poem.txt in copy.txt(upper register)
f_1 = open('dz_lesson_12/txt_file/poem.txt', 'r') 
f_2 = open('dz_lesson_12/txt_file/copy.txt', 'w')
for line in f_1:
    print(f_2.write(line.upper()))

       

