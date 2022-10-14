# Vstup - ošetření, že text bude jen ASCII
# a klíč jen celé a kladné číslo do 26 (máme 26 znaků)
while True:
    text = input("Zadej text, který chceš zakódovat: ")
    if text.isascii():
        while True:
            key = input("Jaký klíč chceš použít? ")
            if key.isdigit() and int(key) > 0 and int(key) % 26 != 0:
                break
            else:
                print('''Klíč musí být celé kladné číslo.
Násobek 26 nic nezašifruje.''')
        break
    print("Bohužel text obsahuje nepovolené znaky, které nejsou ASCII.")
# Šifra - velká písmena 65 - 90, malá písmena 97 - 122 (26 písmen)
new_text = ""
for i in range(len(text)):
    char = text[i]
    if (char.isupper()):
        new_text += chr((ord(char) + int(key) - 65) % 26 + 65)
    elif (char.islower()):
        new_text += chr((ord(char) + int(key) - 97) % 26 + 97)
    else:
        new_text += chr(ord(char))
print(new_text)