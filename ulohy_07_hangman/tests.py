import pytest
import validation
import ai
import hangman


# Testování vstupu
def test_letter_in_word():
    assert validation.check_string("o", "kočka") == True


def test_insert_1_character():
    assert validation.char_validation("a") == "a"


def test_not_insert_number():
    assert not validation.char_validation("1") == "1"


def test_not_insert_more_characters():
    assert not validation.char_validation("abc") == "abc"


# Testování funkce choose_word
def test_choose_word():
    assert ai.choose_word(["pes", "had"]) == "pes" or "had"


# Testování funkce game_field
def test_length_field():
    assert ai.load_field("kočka") == "_ _ _ _ _"


# Testování vypsání písene na pozici
def test_index_letter():
    assert hangman.change("_ _ _", "pes", "e") == "_ e _"
