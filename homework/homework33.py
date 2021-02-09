'''
Napisz funkcję, która sprawdzi, czy kod pocztowy podany przez użytkownika ma właściwy format.
W przypadku błędnego kodu pocztowego, program powinien zgłaszać wyjątek NiepoprawnyKodPocztowy.
'''

class NiepoprawnyKodPocztowy(Exception):
    pass

def check_code():
    while True:
        postal_code = input("Wpisz kod pocztowy: ")
        try:
            check1 = postal_code[2]
            check1 == "-"
            check2 = postal_code.split("-")
            check3 = check2[0]
            check4 = check2[1]
            if check3.isdigit() and check4.isdigit() == True:
                print(postal_code)
                break
            raise Exception("Nie poprawny kod!")
        except Exception as wyjatek:
            print("Złapaliśmy wyjątek o następującej treści:", wyjatek)
        except ValueError:
                print("Nie poprawny kod!")
                continue
        except AttributeError:
             print("Nie poprawny kod!")
             continue

check_code()

