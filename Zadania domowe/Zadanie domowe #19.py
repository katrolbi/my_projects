'''
Napisz program, który policzy różnice w pensji pomiędzy 3 pracownikami. Program powinien:
przyjąć 3 liczby oznaczające pensje każdego z nich
zwrócić różnicę między największą a najmniejszą z nich
obliczenia powinny odbywać się w ramach funkcji

Jak zmienisz program, żeby została zwrócona różnica między środkową a najniższą pensją?
'''

def diff_in_salary():
    salary1 = int(input("Podaj pierwszą pensję w złotówkach: "))
    salary2 = int(input("Podaj drugą pensję w złotówkach: "))
    salary3 = int(input("Podaj trzecią pensję w złotówkach: "))
    diff = max(salary1, salary2, salary3) - min(salary1, salary2, salary3)
    print(diff)

diff_in_salary()


list_of_salary = []
def diff_in_salary2():
    for i in range(3):
        salary = int(input("Podaj pensję w złotówkach: "))
        list_of_salary.append(salary)
    list_of_salary2 = sorted(list_of_salary)
    diff2 = list_of_salary2[2] - list_of_salary2[1]
    print(diff2)

diff_in_salary2()

