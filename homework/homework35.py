'''
Rozszerzenie zadania z zajęć
Do klasy Książka/Book dopisz metodę, która ją opisze. Dodatkowo stwórz metodę, który pozwoli na zmianę gatunku książki.
'''

import datetime
class Book:
    def __init__(self, title, author, year, genre, pages):
        today = datetime.date.today()
        self.title = title
        self.author = author
        if year > today.year:
            raise ValueError(f"Release year can't be greater than {today.year}")
        self.year = year
        self.genre = genre
        if pages < 0:
            raise ValueError(f"Pages must be a number greater than 0")
        self.pages = pages


def describe_book(book):
    print(f"Książka {book.title} została napisana przez {book.author}")


def change_genre(self):
    self.genre = {
        1: "kryminał",
        2: "horror",
        3: "romans"
    }

    describe_book(b1)
    print(self.genre)

    while True:
        choice = input("Jeśli chcesz zmienić gatunek ksiażki wybierz któryś z wymienionych powyżej: ")
        try:
            choice2 = int(choice)
            if choice2 == 1:
                new_genre = self.genre[choice]
                print(new_genre)
            if choice2 == 2:
                new_genre = self.genre[choice]
                print(new_genre)
            if choice2 == 3:
                new_genre = self.genre[choice]
            print(f"Gatunek tej opowieści został zmieniony na {new_genre}.")
            break
        except ValueError:
            print("Nie poprawna odpowiedź")
            continue
        except TypeError:
            print("Nie poprawna odpowiedź")
            continue


b1 = Book("Harry Potter", "J.K. Rowling", 2001, "fantasy", 300)
b2 = Book("Wiedźmin", "Andrzej Sapkowski", 2010, "fantasy", 630)

change_genre(b1)