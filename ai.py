from random import randrange
import piskvorky

def tah_pocitace():
    try:
        cislo_policka = piskvorky.retezec.index("o-") + 2
    except ValueError:
        try:
            cislo_policka = piskvorky.retezec.index("-o") + 1
        except ValueError:
                if "xx-" in piskvorky.retezec:
                    cislo_policka = piskvorky.retezec.index("xx-") + 3
                elif "-xx" in piskvorky.retezec:
                    cislo_policka = piskvorky.retezec.index("-xx") + 1
                else:
                    cislo_policka = tah_pocitace_chyba()
    return piskvorky.tah(cislo_policka, "o")

def tah_pocitace_chyba():
    cislo_policka = randrange(18) + 1
    while piskvorky.retezec[cislo_policka - 1] == "x" or piskvorky.retezec[cislo_policka - 1] == "o":
        cislo_policka = randrange(18) + 1
    return cislo_policka