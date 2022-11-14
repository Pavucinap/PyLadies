from random import choice
import os


def load_words():
    filename = "words.txt"
    if os.path.isfile(filename):
        words = open(filename, encoding="utf-8").read().splitlines()
        return words
    else:
        print(f"Bohužel soubor {filename} neexistuje. Vytvoř si ho.")
        exit()


def choose_word(words):
    """Vybere náhodného slovo ze seznamu"""
    return choice(words)


def load_field(word):
    """Vytvoří herní pole dle počtu písmen ve slově"""
    # Metoda vezme všechny a spojí je podle oddělovač, který MUSÍ být uveden (zde " ")
    field = " ".join(len(word) * "_")
    return field
