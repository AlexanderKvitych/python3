number_of_cats = 100
cats_with_hats = []
number_of_laps = 100

for lap in range(1, number_of_laps + 1):
    for cat in range(1, number_of_cats + 1):
        if cat % lap == 0:
            if cat in cats_with_hats:
                cats_with_hats.remove(cat)
            else:
                cats_with_hats.append(cat)
print(cats_with_hats)