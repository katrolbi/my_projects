import trials
print("Witaj w grze wisielec 🙂")
przycisk=input("Naciśniej ENTER aby rozpocząć grę ")

zagadkowe_slowo=["z","w","i","e","r","z","c","h","n","i","c","t","w","o"]
odkryte_slowo = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
print(f"Odgadnij ukryte słowo: {odkryte_slowo}")
smierc=0
strzaly=[]
proby = 14
while True:
    literka = input("Wpisz literkę -> ")
    if literka in strzaly:
        print("Już powtórzyłeś!")
        proby = proby - 1
        print(proby)
        trials.trial(proby)
        if smierc == proby:
            print("GAME OVER")
            break
        continue
    strzaly.append(literka)
    if len(literka) > 1:
        print("Nie możesz wpisywać więcej niż jedną literę !!!")
    literka_znaleziona = literka in zagadkowe_slowo
    if literka_znaleziona:
        pozycja = 0
        for lit in zagadkowe_slowo:
            if literka == lit:
                print(pozycja, lit)
                odkryte_slowo[pozycja] = lit
            pozycja += 1
        print(odkryte_slowo)
        odp=input("Czy już znasz hasło? Wpisz tak lub nie -> ")
        tak = "tak"
        nie = "nie"
        if str(odp) == tak:
            haslo1 = input("Wprowadź hasło: ")
            if list(haslo1) == zagadkowe_slowo:
                print("Brawo! Wygrałeś!")
                break
            else:
                print("Błędne hasło!")
        elif str(odp) == nie:
            print("To zgaduj dalej 🙂")
        else:
            print("Oj chyba nie umiesz czytać lub pisać 🙂 Zapraszam do dalszej gry")
            continue
    else:
        if proby >= 0:
            print("pudło")
            proby = proby - 1
            print(proby)
            trials.trial(proby)
        if smierc == proby:
            print("GAME OVER")
            break
