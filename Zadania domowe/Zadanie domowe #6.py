'''
Zmodyfikuj zadanie 4 w taki sposób, żeby imiona były przechowywane w krotce.

Dla przypomnienia treść zadania 4 poniżej

Napisz program który:
1. Przypisuje zmiennej wartość będącą listą dowolnych elementów (np. imion uczestników zajęć)
2. Wypisuje każde imię tak, żeby zaczynało się od małej litery
3. Sortuje listę alfabetycznie i wypisuje pierwsze imię
'''

lista_imion=("Kasia", "Michał", "Kinga", "Szymon", "Marta", "Wojtek", "Igor", "Dominika")
print(lista_imion)

for imie in lista_imion:
    print(imie.lower())

lista_imion2 = sorted(lista_imion)
print(lista_imion2)

print(lista_imion2[0])