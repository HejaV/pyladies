def nakresli_mapu(souradnice, ovoce, pocet_kroku, pocet_sloupcu, pocet_radku):
    pocet_kroku = pocet_kroku + 1
    seznam_radku = []
    for souradnice_radek in range(pocet_radku):
        radek = []
        for souradnice_sloupec in range(pocet_sloupcu):
            if (souradnice_radek, souradnice_sloupec) in ovoce:
                radek.append('?')
            elif (souradnice_radek, souradnice_sloupec) in souradnice:
                radek.append('X')
            else:
                radek.append('.')
        seznam_radku.append(radek)
    for radek in seznam_radku:
        for znak in radek:
            print (znak, end='')
        print()
    return pocet_kroku


def zadej_smer():
    smer = input('Pro konec hry zadej 0. V pripade pokracovani zadej smer: ')
    smer = smer.strip().lower()
    if smer not in ['v', 'j', 's', 'z', '0']:
        print('To nebyl spravny smer! Zadej znovu!')
    return smer
