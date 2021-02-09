# Wprowadzenie do historii
# Wybór postaci
# min. 3 wybory co do dalszej drogi
# śmierć
# Zakończenie historii


#Wprowadzenie do historii
with open("wprowadzenie.txt", mode='r', encoding="utf-8") as file:
    print(file.read())

# Wybór postaci
import postacie
postac = postacie.postac

from faker import Faker
fake = Faker()

#pierwszy wybor
zadanie1 = input(f'Wchodzisz do oberży. Po zakupie ekwipunku, {fake.name()} pyta cię o pomoc w pozbyciu się szczurów z piwnicy. \n'
                       f'Czy przyjmujesz to zadanie? Wpisz tak lub nie: ')


import bestiariusz
import walka
while True:
      if zadanie1 == "tak":
            print("\nSchodzisz do piwnicy gdzie natknąłeś się na Króla Szczurów i musisz z nim walczyć o swoje życie!\n")
            szczur = bestiariusz.szczur()
            walka.walka(postac, szczur)
      if zadanie1 == "nie":
            break

print("\nWychodzisz z oberży.\n"
      "Kierujesz się w stronę lasu, gdzie masz spotkać się ze swoim przybranym ojcem.\n")

print(f"Po drodze do lasu spotykasz {fake.name()} i dowiadujesz się o tajemniczej jaskini, w której\n"
      f"jak głosi legenda znajduje sie skarb. Jeszcze nikt nie wrócił z niej żywy.")

zadanie_z_jaskinia = input("Czy chcesz odwiedzić tą jaskinię?. Wpisz tak lub nie: ")

while True:
      if zadanie_z_jaskinia == "tak":
            print("Wchodzisz do jaskini.\n"
                  "Z zaskoczenia atakuje Cię bestia...")
            bestia = bestiariusz.bestia()
            walka.walka(postac,bestia)
      if zadanie_z_jaskinia == "nie":
            print("Idziesz na spotaknie z przybranym ojcem")
      break

import Zasadzka
Zasadzka.zasadzka()


import rozdzial1

