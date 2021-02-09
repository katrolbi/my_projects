'''
Napisz program, który:
przyjmuje od użytkownika 3 liczby: dolny zakres, górny zakres oraz ilość liczb
a następnie losuje zadaną ilość liczb z podanego przedziału

Przykład: Użytkownik podaje liczby 1, 20, 5 -> program ma wylosować 5 liczb z zakresu 1-20 (włącznie)
'''

import random

liczby=input("Podaj trzy liczby po przecinku: dolny zakres, górny zakres oraz ilość liczb wylosowaną z podanego przedziału: ")
liczby2=liczby.split(",")
dolny_zakres=int(liczby2[0])
gorny_zakres=int(liczby2[1])
ilosc_liczb=int(liczby2[2])

for i in range(ilosc_liczb):
    losowanie = random.randint(dolny_zakres, gorny_zakres)
    print(losowanie)
