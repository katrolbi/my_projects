'''
Napisz klasę, która będzie zawierała trzy metody

pobierz_napis - pobiera napis od użytkownika
wyswietl_napis - wyświetla wczesniej pobrany napis od uzytkownika
wyswietl_odwrocony_napis

Dla każdego stworzonego obiektu, metoda pobierz_napis może być wywołana tylko raz => próba ponownego
użycia powinna skutkować błędem
'''

class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase

    def get_phrase(self):
        self.phrase = input("Wpisz cokolwiek: ")

    def display_phrase(self):
        print(self.phrase)

    def invert_your_phrase(self):
        print(self.phrase[len(self.phrase):0:-1])


phrase1 = Phrase("phrase")
phrase1.get_phrase()
phrase1.display_phrase()
phrase1.invert_your_phrase()