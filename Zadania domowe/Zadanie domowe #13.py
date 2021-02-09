'''
Rozszerzenie zadania z operacjami matematycznymi:
Napisz program który:
    - Definiuje funkcje zwracające wynik odpowiedniego działania arytmetycznego:
    dodaj()
    odejmij()
    pomnoz()
    podziel()

    - Pobiera od użytkownika dwie liczby
    - Pobiera od użytkownika którą funkcję wywołać
    - Wypisuje na ekran wynik wywołania tej funkcji

R1: Pobieranie danych z punktu 2 powinno następować tak długo aż użytkonik poda poprawną odpowiedź.
Program nie powinien kończyć się błędem z powodu niepoprawnej nazwy operacji.

R2: Rozwiń program o dwa dodatkowe działania:
- poteguj()
- modulo()

R3: Zmodyfikuj krok 2 tak by obie liczby były pobierane przy pomocy pojedynczej instrukcji input().
'''


def add(a, b):
    # result = a+b jakby było coś bardziej skomplikowanego
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

def involution(a, b):
    return a**b

def modulo(a, b):
    return a//b

liczby = input("Podaj dwie liczby po przecinku: ")
liczby2=liczby.split(",")
a=int(liczby2[0])
b=int(liczby2[1])

list_of_operations = ["dodawanie", "odejmowanie", "mnożenie", "dzielenie", "potęgowanie", "modulo"]
print(list_of_operations)
while True:
    c= input("Jakie działanie mam wykonać? ")
    if c in list_of_operations:
        break

while True:
    if c == "dodawanie":
        result = add(a, b)
        break
    elif c == "odejmowanie":
        result = substract(a, b)
        break
    elif c == "mnożenie":
        result = multiply(a, b)
        break
    elif c == "dzielenie":
        result = divide(a, b)
        break
    elif c == "potęgowanie":
        result = involution(a, b)
        break
    elif c == "modulo":
        result = modulo(a, b)
        break
    else:
        if c not in ("dodawanie", "odejmowanie", "mnożenie", "dzielenie"):
            print("Błędna komenda! Spróbuj ponownie")
            continue

print(result)
