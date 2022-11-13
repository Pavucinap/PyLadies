from random import choice


def load_words():
    """Vytvoří seznam slov ze souboru"""
    filename = "words.txt"
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
            words = contents.split("\n")
            return words
    except OSError:
        print(f'Soubor {filename} bohužel nelze nalézt.')


def choose_word(words):
    """Vybere náhodného slovo ze seznamu"""
    word = choice(words)
    return word


def load_field(word):
    """Vytvoří herní pole dle počtu písmen ve slově"""
    field = "_" + (len(word) - 1) * " _"
    return field
