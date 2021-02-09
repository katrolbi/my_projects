'''
Napisz program, który zliczy ile razy powtarza się każde ze słów z wybranej przez Ciebie piosenki.
'''

tekst_piosenki="Led Zeppelin - Ramble On\n" \
               "Leaves are falling all around\n" \
               "It's time I was on my way\n" \
               "Thanks to you I'm much obliged\n" \
               "For such a pleasant stay\n" \
               "But now it's time for me to go\n" \
               "The autumn moon lights my way\n" \
               "For now I smell the rain\n" \
               "And with it pain\n" \
               "And it's headed my way\n" \
               "Ah, sometimes I grow so tired\n" \
               "But I know I've got one thing I got to do\n" \
               "Ramble on\n" \
               "And now's the time, the time is now\n" \
               "To sing my song\n" \
               "I'm goin' 'round the world, I got to find my girl\n" \
               "On my way\n" \
               "I've been this way ten years to the day\n" \
               "Ramble on\n" \
               "Gotta find the queen of all my dreams\n" \
               "Got no time for spreadin' roots\n" \
               "The time has come to be gone\n" \
               "And thoough our health we drank a thousand times\n" \
               "It's time to ramble on\n" \
               "Ramble on\n" \
               "And now's the time, the time is now\n" \
               "To sing my song\n" \
               "I'm going 'round the world, I got to find my girl\n" \
               "On my way\n" \
               "I've been this way ten years to the day\n" \
               "I gotta ramble on\n" \
               "I gotta find the queen of all my dreams\n" \
               "I ain't tellin' no lie\n" \
               "Mine's a tale that can't be told\n" \
               "My freedom I hold dear\n" \
               "How years ago in days of old\n" \
               "When magic filled the air\n" \
               "'T was in the darkest depths of Mordor\n" \
               "I met a girl so fair\n" \
               "But Gollum, and the evil one\n" \
               "Crept up and slipped away with her\n" \
               "Her, her, yeah\n" \
               "Ain't nothing I can do, no\n" \
               "I guess I keep on rambling\n" \
               "I'm gonna, yeah, yeah, yeah\n" \
               "Sing my song (I gotta find my baby)\n" \
               "I gotta ramble on, sing my song\n" \
               "Gotta work my way around the world baby, baby\n" \
               "Ramble on, yeah\n" \
               "Doo, doo, doo, doo, doo, my baby\n" \
               "Doo, doo, doo, doo\n" \
               "Doodoo doodoo doodoo doodoo doodoo\n" \
               "I gotta keep searching for my baby\n" \
               "(Baby, baby, baby, baby, baby, baby)\n" \
               "I gotta keep-a-searchin' for my baby\n" \
               "(My, my, my, my, my, my, my baby)\n" \
               "Yeah yeah, yeah yeah, yeah yeah yeah\n" \
               "Yeah yeah yeah yeah yeah yeah yeah\n" \
               "I can't find my bluebird\n" \
               "I listen to my bluebird sing\n" \
               "I can't find my bluebird\n" \
               "I keep rambling, baby\n" \
               "I keep rambling, baby"

liczba_wystapien_slow={}

tekst_piosenki=tekst_piosenki.replace(",", " ")
print(tekst_piosenki)
lista_slow=tekst_piosenki.split()
print(lista_slow)
for slowo in lista_slow:
    liczba_wystapien=liczba_wystapien_slow.get(slowo, 0)
    liczba_wystapien_slow[slowo]=liczba_wystapien +1
    print(liczba_wystapien_slow)
