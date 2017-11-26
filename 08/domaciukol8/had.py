from uloha10 import nakresli_mapu, zadej_smer
from uloha11 import pohyb, dalsi_ovoce, pridej_ovoce


pocet_sloupcu = int(input('Zadej pocet sloupcu  mensi nez 41: '))
if pocet_sloupcu <= 0 or pocet_sloupcu >= 41:
    print('Mimo povoleny rozsah')
    exit()
pocet_radku = int(input('Zadej pocet radku vetsi nebo rovno 4 mensi nez 41: '))
if pocet_radku <= 3 or pocet_radku >= 41:
    print('Mimo povoleny rozsah')
    exit()
souradnice = [(0,0),(1,0),(2,0)]
ovoce = []
pridej_ovoce(ovoce, souradnice, pocet_sloupcu, pocet_radku)
pocet_kroku = 0
nakresli_mapu([(0,0),(1,0),(2,0)], ovoce, pocet_radku, pocet_sloupcu, pocet_radku)
smer = ''
while (smer != '0'):
    smer = zadej_smer()
    pohyb(souradnice, ovoce, smer, pocet_sloupcu, pocet_radku)
    pocet_kroku = nakresli_mapu(souradnice, ovoce, pocet_kroku, pocet_sloupcu, pocet_radku)
    dalsi_ovoce(pocet_kroku, ovoce, souradnice, pocet_sloupcu, pocet_radku)
