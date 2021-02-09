'''
Zapytaj użytkownika o przykładowe zdanie, a następnie wyświetl w konsoli co drugi znak, który występuje w tym
zdaniu z zamienioną wielkością liter, np.

dla zdania "Ala ma kota", chcemy otrzymać "aAM OA",

a dla zdania "abcdefghijkl" => "ACEGIK"
'''

zdanie=input("Napisz swoje zdanie -> ")

print(zdanie[::2].swapcase())
