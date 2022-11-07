import pytest
import piskvorky
import util
import ai

# Testování funkce, která vyhodnotí výsledek
def test_vyhodnoceni1():
    assert piskvorky.vyhodnot("----xxx-------------") == "x"

def test_vyhodnoceni2():
    assert piskvorky.vyhodnot("----x-x------ooo----") == "o"

def test_vyhodnoceni3():
    assert piskvorky.vyhodnot("xxooxxooxxooxxooxxoo") == "!"

# Testování, zda se symbol hráče zapíše na správnou pozici
def test_pozice1():
    assert util.tah(20 * "-", "x", 15) == "---------------x----"

def test_pozice2():
    assert util.tah(20 * "-", "o", 10) == "----------o---------"

# Testování špatného zadání pozice (mimo rozsah, na obsazenou pozici)
def test_tah_hrac_chyba1():
    with pytest.raises(IndexError):
        util.tah("----x-x------ooo----", "x", 25)

def test_tah_hrac_chyba2():
    with pytest.raises(RuntimeError):
        util.tah("----x-x------ooo----", "x", 4)

# Testování, že počítač nezadá symbol do plného pole
def test_tah_pocitace_chyba():
    with pytest.raises(RuntimeError):
        ai.tah_pocitace("oxoxoxoxoxoxoxoxoxox", "o")