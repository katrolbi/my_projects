import random
import sys
import time

def wyswiel_napis(napis):
    for litera in napis:
        print(litera, end="")
        time.sleep(0.2)

def function_assertion_error(hp_postaci):
    if hp_postaci <= 0:
        wyswiel_napis("\nUmierasz... To koniec twojej przygody.\n")
        sys.exit()

def walka(postac, bestia):
    hp_postaci = postac.hp
    hp_bestii = bestia.get('hp')
    odp_postaci = postac.odp
    odp_bestii = bestia.get('odp')
    atk_postaci = postac.atk
    atk_bestii = bestia.get('atk')

    for i in range(99):
        atak = random.randint(0, 1)
        if i % 2 == 0:
            print('Postać atakuje!\n')
            if atak == 0:
                print("Nie trafiłeś...\n")
            elif atak == 1:
                print("Bestia oberwała!\n")
                hp_bestii = hp_bestii - (atk_postaci - odp_bestii)
                if hp_bestii <= 0:
                    print("Bestia umiera!\n")
                    break
        else:
            print('Bestia atakuje!\n')
            if atak == 0:
                print("Nie trafiła...\n")
            elif atak == 1:
                print("Oberwałeś!\n")
                hp_postaci = hp_postaci - (atk_bestii - odp_postaci)
                function_assertion_error(hp_postaci)


'''
import time

def wyswiel_napis(napis):
    for litera in napis:
        print(litera, end="")
        time.sleep(0.5)
'''

if __name__ == '__main__':
    postac = {'klasa': 'Wojownik',
              'hp': 12,
              'odp': 4,
              'atk': 7}
    bestia = {'klasa': 'Kobolt',
              'hp': 8,
              'odp': 2,
              'atk': 6}
    def walka(postac, bestia):


        hp_postaci= postac.get('hp')
        hp_bestii = bestia.get('hp')
        odp_postaci=postac.get('odp')
        odp_bestii=bestia.get('odp')
        atk_postaci=postac.get('atk')
        atk_bestii=bestia.get('atk')

        for i in range(99):
            atak = random.randint(0, 1)
            if i % 2 == 0:
                print('atak postaci')
                if atak == 0:
                    print("Nie trafiłeś...")
                elif atak == 1:
                    print("Trafiono")
                    hp_bestii = hp_bestii - (atk_postaci - odp_bestii)
                    if hp_bestii <= 0:
                        print("bestia przegrywa")
                        break
            else:
                print('atak bestii')
                if atak == 0:
                    print("Nie trafiła...")
                elif atak == 1:
                    print("Dostałeś")
                    hp_postaci = hp_postaci - (atk_bestii - odp_postaci)
                    if hp_postaci <= 0:
                        print("postać przegrywa")
                        break

                        def function_assertion_error(hp_postaci):
                            assert hp_postaci > 0
                            print("\nWychodzisz z oberży.\n"
                                  "Kierujesz się w stronę lasu, gdzie masz spotkać się ze swoim przybranym ojcem.\n")
                            return postac.hp

                #     atk_postaci + random.randint(1,6) - odp_bestii = biały_atak_postaci
                #     biały_atak_postaci - hp_bestii > 0
                # elif hp_bestii == 0:
                #     print("bestia padła. Wygrałeś")
                #     break

