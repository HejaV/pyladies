from random import randrange
from uloha10 import nakresli_mapu

def pridej_ovoce(ovoce, souradnice, pocet_sloupcu, pocet_radku):
    if len(souradnice+ovoce)< pocet_sloupcu*pocet_radku:
        x = randrange(pocet_radku)
        y = randrange(pocet_sloupcu)
        while ((x,y) in souradnice + ovoce):
            x = randrange(pocet_radku)
            y = randrange(pocet_sloupcu)
        ovoce.append((x,y))
    else:
        print('Vyhral jsi!')
        exit()




def dalsi_ovoce(pocet_kroku, ovoce, souradnice, pocet_sloupcu, pocet_radku):
    if (pocet_kroku % 5 == 0):
        pridej_ovoce(ovoce, souradnice, pocet_sloupcu, pocet_radku)
        print(ovoce)


def pohyb(souradnice, ovoce, smer, pocet_sloupcu, pocet_radku):
    x = 0
    y = 0
    (r,sl) = souradnice.pop()
    souradnice.append((r,sl))
    print('pred ovoce', ovoce)
    if smer == 'v':
        if (r,sl+1) in ovoce and ((sl+1) < pocet_sloupcu) and ((r,sl+1) not in souradnice):
            i = ovoce.index((r,sl+1))
            del ovoce[i]
            souradnice.append((r,sl+1))
            pridej_ovoce(ovoce, souradnice, pocet_sloupcu, pocet_radku)
        elif (r, sl+1) not in ovoce and ((sl+1) < pocet_sloupcu) and ((r,sl+1) not in souradnice):
            souradnice.append((r,sl+1))
            del souradnice[0]
        elif sl+1 >= pocet_sloupcu or ((r,sl+1) in souradnice):
            print('Game over!')
            exit()
    elif smer == 's':
        if (r-1,sl) in ovoce and ((r-1) >= 0) and ((r-1,sl) not in souradnice):
            i = ovoce.index((r-1,sl))
            del ovoce[i]
            souradnice.append((r-1,sl))
            pridej_ovoce(ovoce, souradnice, pocet_sloupcu, pocet_radku)
        elif (r-1,sl) not in ovoce and ((r-1) >= 0) and ((r-1,sl) not in souradnice):
            souradnice.append((r-1,sl))
            del souradnice[0]
        elif r-1 < 0 or ((r-1,sl) in souradnice):
            print('Game over!')
            exit()
    elif smer == 'z':
        if (r,sl-1) in ovoce and ((sl-1) >= 0) and ((r,sl-1) not in souradnice):
            i = ovoce.index((r,sl-1))
            del ovoce[i]
            souradnice.append((r,sl-1))
            pridej_ovoce(ovoce, souradnice, pocet_sloupcu, pocet_radku)
        elif (r,sl-1) not in ovoce and ((sl-1) >= 0) and ((r,sl-1) not in souradnice):
            souradnice.append((r,sl-1))
            del souradnice[0]
        elif sl-1 < 0 or ((r,sl-1) in souradnice):
            print('Game over!')
            exit()
    elif smer == 'j':
        if (r+1,sl) in ovoce and ((r+1) < pocet_radku )and ((r+1,sl) not in souradnice):
            i = ovoce.index((r+1,sl))
            del ovoce[i]
            souradnice.append((r+1,sl))
            pridej_ovoce(ovoce, souradnice, pocet_sloupcu, pocet_radku)
        elif (r+1,sl) not in ovoce and ((r+1) < pocet_radku) and ((r+1,sl) not in souradnice):
            souradnice.append((r+1,sl))
            del souradnice[0]
        elif r+1 >= pocet_radku or ((r+1,sl) in souradnice):
            print('Game over!')
            exit()
    elif smer == '0':
        print('Koncis hru, nechces pokracovat')
    print('po ovoce', ovoce)
