import random

postacie={
    '1' : "Wojownik",
    '2' : "Łucznik",
    '3' : "Mag"
}

hp_postaci={
    '1' : 12,
    '2' : 10,
    '3' : 8
}

odp_postaci={
    '1' : 4,
    '2' : 3,
    '3' : 2
}

atk_postaci={
    '1' : 2,
    '2' : 3,
    '3' : 5
}

print(postacie)

def postac():
    wybrana_postac= input("Wybierz klasę postaci: 1, 2 lub 3 -> ")
    if wybrana_postac in postacie:
        hp = hp_postaci.get(wybrana_postac)
        odp = odp_postaci.get(wybrana_postac)
        atk = atk_postaci.get(wybrana_postac) + random.randint(2,6)
        wybrana = {f"klasa":postacie.get(wybrana_postac),"hp":hp,"odp":odp,"atk":atk}
        print(f"Wybrana przez ciebie klasa postaci to {postacie.get(wybrana_postac)} i posiada {hp} Hp, {odp} odporności i {atk} siły ataku.")
    return wybrana


'''
while True:
    print(postacie)
    nr_postaci = input("Wybierz postać wpisując numer od 1 - 3: ")
    if nr_postaci in postacie:
        Hp = hp_postaci.get(nr_postaci)
        Odp = odp_postaci.get(nr_postaci)
        atk = atk_postaci.get(nr_postaci)
        for i in range(0,1):
            atak_random = random.randint(0,6)
            print(f"twoj rzut na statystyke ataku wyszedl {atak_random}")
            odpowiedz = input("Czy chcesz powtórzyc rzut? Jesli chcesz to wpisz 'tak' , jesli nie nic nie wpisuj:  ")
            if odpowiedz == "tak":
                continue
            else:
                print("Wybrałeś rzuty albo wykorzystałeś rzuty powodzenia !!")
                break

        Atk = atk + atak_random
        print(Atk)
    break
'''
