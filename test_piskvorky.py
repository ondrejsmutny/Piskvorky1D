import ai
import piskvorky

def test_tah_pocitace_1():
    piskvorky.retezec = "o-------------------"
    assert ai.tah_pocitace() == "oo------------------"

def test_tah_pocitace_2():
    piskvorky.retezec = "-------------------o"
    assert ai.tah_pocitace() == "------------------oo"

def test_tah_pocitace_3():
    piskvorky.retezec = "-----------------xx-"
    assert ai.tah_pocitace() == "-----------------xxo"

def test_tah_pocitace_4():
    piskvorky.retezec = "-----------------xxo"
    assert ai.tah_pocitace() == "----------------oxxo"

def test_vyhodnot_1():
    piskvorky.retezec = "--------ooo---------"
    assert piskvorky.vyhodnot(piskvorky.retezec) == "o"

def test_vyhodnot_2():
    piskvorky.retezec = "-xxx----------------"
    assert piskvorky.vyhodnot(piskvorky.retezec) == "x"

def test_vyhodnot_3():
    piskvorky.retezec = "oxoxoxoxoxoxoxoxoxox"
    assert piskvorky.vyhodnot(piskvorky.retezec) == "!"

def test_vyhodnot_4():
    piskvorky.retezec = "----o-----------x---"
    assert piskvorky.vyhodnot(piskvorky.retezec) == "-"

def test_tah_1():
    piskvorky.retezec = "----o-----------x---"
    assert piskvorky.tah(2,"o") == "-o--o-----------x---"

def test_tah_2():
    piskvorky.retezec = "-o--o-----------x---"
    assert piskvorky.tah(18,"x") == "-o--o-----------xx--"

def test_tah_hrace_1(monkeypatch):
    piskvorky.retezec = "--------------------"
    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert piskvorky.tah_hrace() == "-x------------------"

def test_tah_hrace_2(monkeypatch):
    piskvorky.retezec = "--------------------"
    monkeypatch.setattr('builtins.input', lambda _: "20")
    assert piskvorky.tah_hrace() == "-------------------x"

