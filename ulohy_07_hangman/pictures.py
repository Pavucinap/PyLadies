def draw_picture(fail_number):
    try:
        print(picture_list[fail_number])
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

picture_list = [pic0, pic1, pic2, pic3, pic4, pic5, pic6, pic7, pic8, pic9]
