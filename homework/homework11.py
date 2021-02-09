'''
Napisz program, który przyjmuje na wejściu napis i wypisuje:

"wiek musi być liczbą" jeśli wiek nie jest liczbą
"wiek nie może być mniejszy od 0" jeśli wiek jest liczbą ujemną
"parzysty" jeśli wiek jest parzysty
'''

while True:
    wiek=input("Ile masz lat? ")
    if wiek.lstrip("-").isnumeric():
        print("OK. Wiek jest liczbą.")
        wiek=int(wiek)
        if wiek <= 0:
            print("Wiek nie może być mniejszy lub równy zeru!")
        else:
            print("Prawidłowy wiek.")
        if wiek % 2 == 0:
            print("Wiek jest liczbą parzystą.")
        else:
            print("Wiek jest liczbą nieparzystą")
        break
    else:
        print("Wiek nie jest liczbą!")
        continue
