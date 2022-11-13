def draw_picture(fail_number):
    try:
        print(picture_dictionary[fail_number])
    except IndexError:
        print("Tolik obrázků není k dispozici.")


pic0 = """







~~~~~~~"""

pic1 = """
+
|
|
|
|
|
~~~~~~~"""

pic2 = """
+---.
|
|
|
|
|
~~~~~~~"""

pic3 = """
+---.
|   |
|
|
|
|
~~~~~~~"""

pic4 = """
+---.
|   |
|   O
|
|
|
~~~~~~~"""

pic5 = """
+---.
|   |
|   O
|   |
|
|
~~~~~~~"""

pic6 = """
+---.
|   |
|   O
| --|
|
|
~~~~~~~"""

pic7 = """
+---.
|   |
|   O
| --|--
|
|
~~~~~~~"""

pic8 = """
+---.
|   |
|   O
| --|--
|  /
|
~~~~~~~"""

pic9 = """
+---.
|   |
|   O
| --|--
|  / \\
|
~~~~~~~"""

picture_dictionary = {
    0: pic0,
    1: pic1,
    2: pic2,
    3: pic3,
    4: pic4,
    5: pic5,
    6: pic6,
    7: pic7,
    8: pic8,
    9: pic9}
