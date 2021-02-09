'''
Napisz program, który otwiera plik przewoz_osob_gdynia.csv, a następnie wyświetla daty
dla których liczba osób była największa i najmniejsza.
'''

import csv
import collections


passenger_transport = collections.namedtuple("passenger_transport", ["tys_osob", "month"])
with open("przewoz_osob_gdynia.csv", mode='r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    passengers = []

    for passenger in reader:
        nr_people = passenger_transport(passenger[0], passenger[1])
        passengers.append((float(nr_people.tys_osob), nr_people.month))
    print(f"Największą liczbę ludzi {max(passengers)[0]} przewieziono {(max(passengers)[1])}, "
          f"a najmniejszą ilość ludzi {min(passengers)[0]} przewieziono {min(passengers)[1]}.")
