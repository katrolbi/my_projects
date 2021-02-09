'''
Napisz program, który wyświetli połączone linijki z dwóch plików, np.
Pierwsza linijka z pierwszego pliku. Pierwsza linijka z drugiego pliku
Druga linijka z pierwszego pliku. Druga linijka z drugiego pliku
Trzecia linijka z pierwszego pliku. Trzecia linijka z drugiego pliku
'''


with open("first_line", mode="r", encoding="utf-8") as file:
    lines = []
    for line in file:
        lines.append(line)
    with open("second_line", mode="r", encoding="utf-8") as second_file:
        next_lines =[]
        for next_line in second_file:
            next_lines.append(next_line)
    with open("third_line", mode="r", encoding="utf-8") as third_file:
        another_lines =[]
        for another_line in third_file:
            another_lines.append(another_line)
    print(f"{lines[0]} \n"
          f"{next_lines[0]}\n"
          f"{another_lines[0]}")