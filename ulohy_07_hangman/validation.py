import string


def char_validation(character):
    """Ověření zadaého písmene."""
    alphabet = "ěščřžýáíéúůóťď" + string.ascii_lowercase
    # ošetření, aby hráč zadal jen jeden znak
    if len(character) == 1:
        # ošetření, aby hráč zadal jen písmeno
        if character not in alphabet:
            print("Tvůj zvolený znak není malé písmeno.")
            return False

    else:
        print("Můžeš vložit jen 1 malé písmeno.")
        return False

    return character


def check_string(letter, text):
    """Zjistí, zda je písmeno v řetězci"""
    if letter in text:
        return True
    return False
