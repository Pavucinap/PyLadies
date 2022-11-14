import os


def about_game():
    if os.path.isfile("README.md"):
        about = open("README.md", encoding="utf-8").read()
        print(about)
    else:
        print("""
        Vítejte ve hře Šibenice

        Specifikace pro tuto hru:
            - slova jsou složena z pouze z malých písmen (včetně českých znaků)
            - hra končí po úspěšném uhádnutí nebo po 9 neúspěšných pokusech
            - písmeno "ch" jsou 2 znaky, znak "c" a znak "h"
            - písmeno s háčkem a bez háčku není to stejné, např. "c" a "č" jsou různé znaky
        """)
