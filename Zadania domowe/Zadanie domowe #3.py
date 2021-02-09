'''
Napisz program, który pozwoli wygenerować krótkie opowiadanie.
Na początku programu zadeklaruj przynajmniej 5 zmiennych, które będą wykorzystane w tym tekście
( jeśli nie masz pomysłu, mogą to być np. imię, wiek, kolor włosów, wybrany dzień tygodnia, pora roku )
Edycja wybranych zmiennych powinna zmieniać treść opowiadania.
'''


dzien =input("Którego dnia? -> ")
co=input("Dramat czego? -> ")
kto=input("Dzięki czemu go poznałeś? Dzięki -> ")
kto2=input("Co je zjada? -> ")
co2=input("Co takiego zjadają? -> ")



print(f'Codziennie dowiadywałem się czegoś nowego o planecie, o wyjeździe, o podróży. Wiadomości te gromadziły się '
      f'z wolna i przypadkowo. I tak {dzien} dnia poznałem dramat {co}. W tym przypadku stało się to '
      f'dzięki {kto}. Mały Książę spytał mnie nagle, jakby w coś zwątpił:\n'
      f'- Czy to prawda, że {kto2} zjadają {co2}?\n'
      f'- Tak, to prawda.\n'
      f'- O, to bardzo się z tego cieszę.\n'
      f'- Nie rozumiałem, jakie znaczenie może mieć wiadomość, że {kto2} zjadają {co2}. Ale Mały Książę dodał:\n'
      f'- Wobec tego one jedzą także {co}?''')

print(f'Codziennie dowiadywałem się czegoś nowego o planecie, o wyjeździe, o podróży. Wiadomości te gromadziły się '
      f'z wolna i przypadkowo. I tak {dzien} dnia poznałem dramat {co}. W tym przypadku stało się to '
      f'dzięki {kto}. Mały Książę spytał mnie nagle, jakby w coś zwątpił:\n'
      f'- Czy to prawda, że {kto2} zjadają {co2}?\n'
      f'- Tak, to prawda.\n'
      f'- O, to bardzo się z tego cieszę.\n'
      f'- Nie rozumiałem, jakie znaczenie może mieć wiadomość, że {kto2} zjadają {co2}. Ale Mały Książę dodał:\n'
      f'- Wobec tego one jedzą także {co}?'''[::-1])