import pytest
import piskvorky
import util
import ai


# Testování funkce, která vyhodnotí výsledek
def test_vyhodnoceni_vyhrava_x():
    assert piskvorky.vyhodnot("----xxx-------------") == "x"


def test_vyhodnoceni_vyhrava_o():
    assert piskvorky.vyhodnot("----x-x------ooo----") == "o"


def test_vyhodnoceni_remiza():
    assert piskvorky.vyhodnot("xxooxxooxxooxxooxxoo") == "!"


# Testování, zda se symbol hráče zapíše na správnou pozici
def test_zadani_x_na_spravnou_pozici():
    assert util.tah(20 * "-", "x", 15) == "---------------x----"


def test_zadani_o_na_spravnou_pozici():
    assert util.tah(20 * "-", "o", 10) == "----------o---------"


# Testování špatného zadání pozice (mimo rozsah, na obsazenou pozici)
def test_tah_hrac_mimo_herni_pole():
    with pytest.raises(IndexError):
        util.tah("----x-x------ooo----", "x", 25)


def test_tah_hrac_na_obsazenou_pozici():
    with pytest.raises(RuntimeError):
        util.tah("----x-x------ooo----", "x", 4)


# Testování, že počítač nezadá symbol do plného pole
def test_tah_pocitace_do_plneho_pole():
    with pytest.raises(RuntimeError):
        ai.tah_pocitace("oxoxoxoxoxoxoxoxoxox", "o")
