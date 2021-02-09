'''
Rozszerzenia do zadania:
Utwórz ręcznie (przy pomocy PyCharm) plik tekstowy. Wpisz do niego 4 dowolne napisy: każdy w nowym wierszu.
Napisz program który odczyta ten plik, wypisze każdy z wierszy i dla każdego wiersza poda jego długość.

Dla każdego wiersza wypisz najczęściej występująca literę.
Wypisz także najczęściej występujące słowo dla całego pliku.
'''

from collections import Counter

def find_most_common():
     with open("zadanie_domowe.txt", encoding="utf-8") as my_file:
        for line in my_file:
            line1 = line.strip().lower()
            print(line1)
            print(f"{len(line1)}")
            print("_____________")
            line2 = line1.replace(" ", "")
            print(Counter(line2).most_common(1))

        words = list(line.split(" "))
        print(Counter(words).most_common(1))

find_most_common()




