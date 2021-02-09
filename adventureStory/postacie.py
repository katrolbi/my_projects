import random

def choice():
    while True:
        try:
            wybrana_postac = int(input("Wybierz klasę postaci wpisując jej numer: 1 - Wojownik, 2 - Łucznik lub 3 - Mag -> "))
        except ValueError:
            print("Wprowadź wartość numeryczną np: 1, 2 lub 3")
        else:
            break
    return wybrana_postac

class Characters:
    def __init__(self, hp, odp, atk):
        self.hp = hp
        self.odp = odp
        self.atk = atk + random.randint(2,6)

class Wojownik(Characters):
    def __init__(self, hp, odp, atk):
        super().__init__(hp, odp, atk)


    def describe_wojownik(self):
        choice1 = {f"klasa" : "Wojownik", "hp": {self.hp}, "odp": {self.odp}, "atk": {self.atk}}
        print(
                f"Wybrana przez ciebie klasa postaci to Wojownik, który posiada {self.hp} Hp,"
                f" {self.odp} odporności i {self.atk} siły ataku.")
        return choice1\


class Lucznik(Characters):
    def __init__(self, hp, odp, atk):
        super().__init__(hp, odp, atk)


    def describe_lucznik(self):
        if wybrany_index_postaci == 2:
            choice2 = {f"klasa" : "Łucznik", "hp": {self.hp}, "odp": {self.odp}, "atk": {self.atk}}
            print(
                f"Wybrana przez ciebie klasa postaci to Łucznik, który posiada {self.hp} Hp,"
                f" {self.odp} odporności i {self.atk} siły ataku.")
        return choice2

class Mag(Characters):
    def __init__(self, hp, odp, atk):
        super().__init__(hp, odp, atk)

    def describe_mag(self):
        if wybrany_index_postaci == 3:
            choice3 = {f"klasa" : "Mag", "hp": {self.hp}, "odp": {self.odp}, "atk": {self.atk}}
            print(
                f"Wybrana przez ciebie klasa postaci to Mag, który posiada {self.hp} Hp,"
                f" {self.odp} odporności i {self.atk} siły ataku.")
        return choice3

wybrany_index_postaci = choice()
if wybrany_index_postaci == 1:
    postac = Wojownik(14, 5, 4)
    postac.describe_wojownik()
elif wybrany_index_postaci == 2:
    postac = Lucznik(12, 4, 5)
    postac.describe_lucznik()
elif wybrany_index_postaci == 3:
    postac = Mag(10, 3, 7)
    postac.describe_mag()


