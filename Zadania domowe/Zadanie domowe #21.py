'''
Napisz program który pobiera od użykownika datę urodzin. Następnie wyświetla na ekranie wiek danej osoby.
'''

import datetime

def user_age():
    birth_date = input("Wpisz swoje datę urodzenia w podanej formie rrrr-mm-dd: ")
    birth_day2 = birth_date.split("-")
    py_date = datetime.date(int(birth_day2[0]),int(birth_day2[1]),int(birth_day2[2]))
    today = datetime.date.today()
    print(f"Masz {today.year - py_date.year} lat i {today.month - py_date.month} miesiece/miesięcy.")

user_age()

#czy jest prostszy sposób na tą zamianę daty?