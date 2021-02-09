'''
Stwórz klasę Pracownik, która będzie zawierała następujące atrybuty i metody
(a) imię i nazwisko
(a) data zatrudnienia
(a) wypłata podstawowa
(m) oblicz staż pracy
(m) oblicz wypłatę

Następnie stwórz klasę Manager, która będzie dziedziczyła po klasie Pracownik

dodaj atrybut przechowujący datę objęcia stanowiska
nadpisz atrybut wypłata podstawowa poprzez przypisanie do niego nowej wartości
nadpisz metodę do obliczania wypłata, żeby uwzględnić bonus za stanowisko (np. mnożnik 1.5x)
dodaj nową metodę, która obliczy jak długa dana osoba przebywa na stanowisku
'''
import datetime

class Employee:
    def __init__(self, first_name, last_name, hire_date, basic_payout):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.basic_payout = basic_payout

    def seniority(self):
        hd = self.hire_date.split("-")
        hd2 = datetime.date(int(hd[0]),int(hd[1]),int(hd[2]))
        today = datetime.date.today()
        print(f"Twój staż pracy to {today.year - hd2.year} lat i {today.month - hd2.month} miesięce/y.")

    def salary(self):
        hd = self.hire_date.split("-")
        hd2 = datetime.date(int(hd[0]),int(hd[1]),int(hd[2]))
        today = datetime.date.today()
        if (today.year - hd2.year) >= 10:
            big_salary = round(self.basic_payout * 1.2)
            print(f"Dostajesz {big_salary} za staż pracy.")
        else:
            print(f"Za taki staż pracy ostaniesz podstawową pensję {self.basic_payout}.")

class Manager(Employee):
    def __init__(self, first_name, last_name, hire_date, basic_payout, management_date):
        super().__init__(first_name, last_name, hire_date, basic_payout)
        self.basic_payout = basic_payout*1.5
        self.management_date = management_date

    def promotion_date(self):
        md = self.management_date.split("-")
        md2 = datetime.date(int(md[0]),int(md[1]),int(md[2]))
        today = datetime.date.today()
        print(f"Twój staż pracy jako menadżer to {today.year - md2.year} lat i {today.month - md2.month} miesięce/y.")

employee = Employee("Jan", "Kowalski", "2000-01-01", 3000)
employee.seniority()
employee.salary()

manager = Manager("Jan", "Kowalski", "2005-01-01", 3000, "2015-01-01")
manager.salary()
manager.promotion_date()
