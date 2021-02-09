'''
Napisz program, który zapyta użytkownika o jakieś zdanie, a następnie policzy i wypisze
liczbę małych i dużych liter w tym zdaniu.
'''

zdanie = input("Napisz swoja zdanie: ")

count_small_letters = 0
count_big_letters = 0
for i in zdanie:
    if i.islower():
        count_small_letters = count_small_letters + 1
    elif i.isupper():
        count_big_letters = count_big_letters + 1

print(f"W zdaniu występują {count_big_letters} dużych liter oraz {count_small_letters} małych liter.")