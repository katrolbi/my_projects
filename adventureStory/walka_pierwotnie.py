import random

def walka(postac, bestia):
    hp_postaci = postac.get('hp')
    hp_bestii = bestia.get('hp')
    odp_postaci = postac.get('odp')
    odp_bestii = bestia.get('odp')
    atk_postaci = postac.get('atk')
    atk_bestii = bestia.get('atk')

    for i in range(99):
        atak = random.randint(0, 1)
        if i % 2 == 0:
            print('Postać atakuje!')
            if atak == 0:
                print("Nie trafiłeś...")
            elif atak == 1:
                print("Bestia oberwała!")
                hp_bestii = hp_bestii - (atk_postaci - odp_bestii)
                if hp_bestii <= 0:
                    print("Bestia umiera!")
                    break
        else:
            print('Bestia atakuje!')
            if atak == 0:
                print("Nie trafiła...")
            elif atak == 1:
                print("Oberwałeś!")
                hp_postaci = hp_postaci - (atk_bestii - odp_postaci)
                if hp_postaci <= 0:
                    print("Umierasz...")
                    break



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


