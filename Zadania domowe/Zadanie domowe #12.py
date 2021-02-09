'''
Zmodyfikuj program ze zgadywaniem wylosowanej liczby, tak, żeby użytkownik miał ograniczoną liczbę strzałów (np. 6).
'''

import random
wylosowana_liczba = random.randint(1,101)

for losowa in range(6):
    losowa = input("Wybierz liczbę -> ")
    if int(losowa) == wylosowana_liczba:
        print("Trafiłeś")
        break
    elif int(losowa) > wylosowana_liczba:
        print("Podana liczba jest za duża, spróbuj ponownie")
    elif int(losowa) < wylosowana_liczba:
        print("Podana liczba jest za mała, spróbuj ponownie")
    continue
