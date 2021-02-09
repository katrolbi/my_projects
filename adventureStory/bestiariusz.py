import random

Bestie = {'1':'Minotaur','2':'Goblin','3':'Szkielet','4':'Ghul',
'5':'Kobolt','6':'Szczur_sciekowy','7':'Bandyta','8':'Zjawa','9':'Trol','10':'Wampir','11':'Król_szczurów'}

Hp_Bestii = {'1':18,'2':6,'3':6,'4':10,'5':8,'6':4,'7':12,'8':6,'9':20,'10':16,'11':20}

odp_bestii = {'1':3,'2':2,'3':2,'4':3,'5':2,'6':1,'7':2,'8':1,'9':4,'10':4,'11':4}

Atk_Bestii = {'1':6,'2':4,'3':4,'4':5,'5':4,'6':3,'7':4,'8':5,'9':10,'10':8,'11':7}

def bestia():
    # nr_bestii = str(random.randint(1, 10))
    nr_bestii = str(random.randint(0,10))
    if nr_bestii in Bestie:
        Bestia = Bestie.get(nr_bestii)
        Hp = Hp_Bestii.get(nr_bestii)
        Odp = odp_bestii.get(nr_bestii)
        Atk = Atk_Bestii.get(nr_bestii)
        wybrana = {f"klasa": Bestia, "hp": Hp, "odp": Odp, "atk": Atk}
    print(f"Twój przeciwnik to {Bestia}, z Hp = {Hp},odpornością = {Odp} oraz atakiem = {Atk}")
    return wybrana

def szczur():
    # nr_bestii = str(random.randint(1, 10))
    nr_bestii = '11'
    if nr_bestii in Bestie:
        Bestia = Bestie.get(nr_bestii)
        Hp = Hp_Bestii.get(nr_bestii)
        Odp = odp_bestii.get(nr_bestii)
        Atk = Atk_Bestii.get(nr_bestii)
        wybrana = {f"klasa": Bestia, "hp": Hp, "odp": Odp, "atk": Atk}
    print(f"Twój przeciwnik to {Bestia}, z Hp = {Hp},odpornością = {Odp} oraz atakiem = {Atk}")
    return wybrana
