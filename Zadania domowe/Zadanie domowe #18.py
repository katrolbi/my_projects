'''
Napisz program do generowania haseł o długości zadanej przez użytkownika.
Hasło powinno się zmieniać wraz z każdym uruchomieniem programu.
Pamiętaj, że dobre hasło powinno zawierać zarówno małe jak i duże litery, cyfry oraz znaki specjalne (np. #?%&).
'''
import random
from string import punctuation, ascii_letters, digits
symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()
dl_hasla=int(input("Jakiej długości ma być hasło? "))
password = "".join(secure_random.choice(symbols) for i in range(dl_hasla))
print(password)