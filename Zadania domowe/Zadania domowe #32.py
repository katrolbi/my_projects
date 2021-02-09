'''
Napisz funkcję, która umożliwia użytkownikowi pobranie wartości ze zdefiniowanego wcześniej słownika.

Użytkownik powinien zdecydować spod jakiego klucza ma być odczytana wartość. W przypadku błędnego
klucza, który nie istnieje w danym słowniku, program powinien ponowić pytanie o klucz.

Sytuację z nieistniejącym kluczem obsłuż za pomocą wyjątku
'''

dictionary = {
    "pies" : "dog",
    "kot" : "cat",
    "mysz" : "mouse",
    "chomik" : "hamster",
    "koń" : "horse"
}

def find_your_animal():
    print(dictionary.keys())
    while True:
        animal = input("Wpisz nazwę zwierzęcia z podanego słownika i dowiedz sie jak ono brzmi po angielsku: ")
        try:
            value = dictionary[animal]
            print(value)
            break
        except KeyError:
            print("Takiego zwierzęcia nie ma w słowniku")
            continue

find_your_animal()
