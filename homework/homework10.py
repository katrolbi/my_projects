'''
Napisz program, który pobiera od użytkownika wynik z testu w % i wyświetla odpowiadającą temu wynikowi ocenę.
Przykładowa skala ocen:
91 % – 100 % -> 5
75 % – 90 % -> 4
51 % – 74 % -> 3
30 % – 50 % -> 2
0 % – 29 % -> 1'''

wynik_testu=int(input("Podaj swój wynik testu w % a dowiesz sie jaką ocenę dostałeś: "))

if wynik_testu >= 91:
    print("Dostajesz 5!")
elif 75 <= wynik_testu <= 90:
    print("Dostajesz 4!")
elif 51 <= wynik_testu <= 74:
    print("Dostajesz 3!")
elif 30 <= wynik_testu <= 50:
    print("Dostajesz 2!")
elif 0 <= wynik_testu <= 29:
    print("Dostajesz 1!")