'''
Napisz program który pobiera dane od użytkownika a następnie zlicza liczbę poszczególnych liter.
Podziel go na odpowiednie funkcje których będzie można ponownie użyć (pobierz_dane(), policz_litery(), ...)

Następnie użyj tego programu by wypisać 4 najpopularniejsze litery w "Panu Tadeuszu" (plik pan_tadeusz.txt)
wraz z liczbą ich wystąpień.
pan_tadeusz.txt
'''
# global histogram
from collections import Counter


def zliczanie(linia):
    slownik_wystapien = {}
    for i in linia:
        i = i.lower()
        if i.isalpha():
            if i in slownik_wystapien:
                slownik_wystapien[i] += 1
            else:
                slownik_wystapien[i] = 1
    return slownik_wystapien

def wybieranie_top_czterech_liter(Histogram):
    k = Counter(Histogram)
    high = k.most_common(4)
    return high


with open('pan_tadeusz.txt', encoding=('utf-8')) as f:
    Pan_tadeusz_linia = f.read()
    Pan_tadeusz_linia_histogram = zliczanie(Pan_tadeusz_linia)
    # print(Pan_tadeusz_linia_histogram)
    for i in wybieranie_top_czterech_liter(Pan_tadeusz_linia_histogram):
        print(i[0], " :", i[1], " ")
