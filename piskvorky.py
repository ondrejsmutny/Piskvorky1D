retezec = "--------------------"
import ai

def vyhodnot(retezec):
    if "ooo" in retezec:
        return "o"
    elif "xxx" in retezec:
        return "x"
    elif "-" not in retezec:
        return "!"
    else:
        return "-"

def tah(cislo_policka, symbol):
    global retezec
    zacatek = retezec[:cislo_policka - 1]
    konec = retezec[cislo_policka:]
    retezec = (zacatek + symbol + konec)
    return retezec

def tah_hrace():
    while True:
        cislo_policka = input("Na které políčko chceš hrát?: ")
        try:
            cislo_policka = int(cislo_policka)
            break
        except ValueError:
            print("Zadej číslo 1 - 20")
    while cislo_policka < 1 or cislo_policka > 20:
        print("Zadej číslo 1 - 20")
        cislo_policka = int(input("Na které políčko chceš hrát?: "))
    while retezec[cislo_policka - 1] == "x" or retezec[cislo_policka - 1] == "o":
        print("Vyber neobsazené políčko")
        cislo_policka = int(input("Na které políčko chceš hrát?: "))
    return tah(cislo_policka, "x")

def piskvorky1d():
    while vyhodnot(retezec) == "-":
        print(ai.tah_pocitace())
        if vyhodnot(retezec) == "o":
            print("Vyhrává počítač")
            break
        print(tah_hrace())
        if vyhodnot(retezec) == "x":
            print("Vyhrává hráč")
            break
        if vyhodnot(retezec) == "!":
            print("Remíza")
            break        
    return ""
