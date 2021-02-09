'''
Napisz program, który wyświetli losową linijkę z pliku.
'''

import random

with open("text.txt", mode='r', encoding="utf-8") as file:
    lines = []
    for line in file:
        lines.append(line)
    print(random.choice(lines))
