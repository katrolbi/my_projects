'''
Napisz program, który pyta użytkownika o wyraz / zdanie, a następnie wyświetla informację czy jest ono palindromem czy nie.
'''

string = input("Enter a string: ")
if (string == string[::-1]):
    print("The string is a palindrome")
else:
    print("Not a palindrome")
