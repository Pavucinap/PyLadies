from ai import load_words, choose_word, load_field
from insert_character import char_insert
import pictures
import validation


def validate_input(generated_field, random_word, letter):
    """Ověří, zda může být písmeno zapsáno do herního pole"""
    if validation.check_string(letter, random_word) \
            and not validation.check_string(letter, generated_field):
        return True
    return False


def change(generated_field, random_word, letter):
    """Pokud je písmeno ve slově, zapíše ho na pozici"""
    if validation.check_string(letter, random_word) \
            and not validation.check_string(letter, generated_field):
        position = random_word.index(letter)
        new_field = generated_field[:position * 2] + letter + " " + \
            generated_field[(position * 2) + 2:]
        return new_field


def result(generated_field, random_word):
    """Vyhodnocení hry: pokud "_" není v řetězci, výhra, jinak hra pokračuje"""
    if '_' not in generated_field:
        print(f"\nSkvělě, výhráváš. Hledané slovo bylo: {random_word}")
        return False
    return True


def game():
    """Spuštění hry"""
    fail_counter = 0
    game_word = choose_word(load_words())
    game_field = load_field(game_word)
    while result(game_field, game_word):
        pictures.draw_picture(fail_counter)
        print(f"{game_field}\n")
        letter = char_insert()
        if validate_input(game_field, game_word, letter):
            game_field = change(game_field, game_word, letter)
        else:
            fail_counter += 1
            if fail_counter == 9:
                pictures.draw_picture(fail_counter)
                print(f"Prohrál jsi. Hledané slovo bylo: {game_word}")
                break
            else:
                print(f"\nBohužel {letter} tam není.")
                print(f"Zbývající počet pokusů: {9 - fail_counter}")
