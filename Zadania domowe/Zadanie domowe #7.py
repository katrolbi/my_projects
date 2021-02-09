'''Napisz program, który:
pozwoli użytkownikowi na wprowadzenie wyrazu
następnie policzy i wyświetli wynik punktowy w Scrabble na podstawie wcześniej zdefiniowanej punktacji
np. literka a to 1 punkt, literka b to 3 punkty itd.
-> zadanie można rozwiązać na wiele sposobów, więc do Ciebie zależy wybór jak taka punktacja będzie przechowywana
-> należy uwzględnić, że jakaś literka w wyrazie podanym przez użytkownika nie będzie uwzględniona w punktacji
(można przyjąć, że dostaje on za nią 0 punktów)'''


punktacja = {
    "a": 1,
    "b": 3,
    "c": 2,
    "ć": 6,
    "d": 2,
    "e": 1,
    "ę": 5,
    "f": 5,
    "g": 3,
    "h": 3,
    "i": 1,
    "j": 3,
    "k": 2,
    "l": 2,
    "ł": 3,
    "m": 2,
    "n": 1,
    "ń": 7,
    "o": 1,
    "ó": 5,
    "p": 2,
    "q": 0,
    "r": 1,
    "s": 1,
    "ś": 5,
    "t": 2,
    "u": 3,
    "v": 0,
    "w": 1,
    "x": 0,
    "y": 2,
    "z": 1,
    "ź": 9,
    "ż": 5
}

slowo = input("Wprowadź swój wyraz to otrzymasz łączną punktacje -> ")

def wynik_scrabble(slowo):
    total=0
    for i in slowo:
        i=i.lower()
        total = total + punktacja[i]
    return total

print(wynik_scrabble(slowo))