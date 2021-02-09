'''
Napisz program, który przyjmuje od użytkownika napis składający się ze słów rozdzielonych
myślnikiem, a następnie zwraca napis ze słowami posortowanymi alfabetycznie (również oddzielone myślnikami)

np. kot-pies-albatros-czapla-delfin --> albatros-czapla-delfin-kot-pies
'''

napis= input("Wpisz łańcuch wyrazów oddzielonych myślnikiem: ")
napis2=napis.split("-")
napis3=sorted(napis2)
napis4 = "-".join(napis3)
print(napis4)