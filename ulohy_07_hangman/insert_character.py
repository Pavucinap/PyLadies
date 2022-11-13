import validation


def char_insert():
    """Vložené písmeno s ověřením."""
    while True:
        insert_character = input("Jaké písmeno chceš vložit? ")
        if not validation.char_validation(insert_character):
            continue
        break
    return insert_character
