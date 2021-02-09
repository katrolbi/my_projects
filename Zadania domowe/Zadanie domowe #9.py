'''
Napisz program, który:
    przypisze do zmiennej cenę za litr paliwa
    przypisze do zmiennej średnie spalanie na 100 km
    następnie zapyta użytkownika o cenę, którą jest w stanie zapłacić oraz długość trasy w km, jaką chce pokonać

Program powinien wypisać komunikat z decyzją czy uda się przejechać podaną trasę po zatankowaniu auta za przytoczoną kwotę.
'''

def oblicz_ilosc_paliwa(dl_trasy, sr_spalanie):
    return dl_trasy * sr_spalanie
def oblicz_koszt_paliwa(il_paliwa, cena_za_litr):
    return il_paliwa * cena_za_litr
def oblicz_koszt_podrozy(dl_trasy, sr_spalanie, cena_za_litr):
    il_paliwa= oblicz_ilosc_paliwa(dl_trasy, sr_spalanie)
    koszt_paliwa = oblicz_koszt_paliwa(il_paliwa, cena_za_litr)
    return koszt_paliwa

sr_spalanie=0.07
dl_trasy=100
cena= 4
przeliczony_koszt_podrozy = round(oblicz_koszt_podrozy(dl_trasy, sr_spalanie, cena),2)

na_ile_go_stac = int(input("Ile jesteś w stanie zapłacić za taką podróż? Podaj samą liczbę w zł -> "))

print(f'Koszt takiej podróży to {przeliczony_koszt_podrozy} zł.')

if przeliczony_koszt_podrozy <= na_ile_go_stac:
    print("Stać Cię na taka podróż!")
else:
    print("Nie stać Cię")

