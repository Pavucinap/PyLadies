# Vstup - ošetření, že text bude jen ASCII
# a klíč jen celé a kladné číslo do 26 (máme 26 znaků)
while True:
    text = input("Zadej text, který chceš zakódovat: ")
    if text == "":
        exit()
    elif text.isascii():
        while True:
            key = input("Jaký klíč chceš použít? ")
            if key.isdigit() and int(key) > 0 and int(key) % 26 != 0:
                break
            print("Klíč musí být celé kladné číslo. \n"
                "Násobek 26 nic nezašifruje.")
        break
    print("Bohužel text obsahuje nepovolené znaky, které nejsou ASCII.")

# Šifra - velká písmena 65 - 90, malá písmena 97 - 122 (26 písmen)
a = ord("a")
A = ord("A")
new_text = ""
for char in text:
    if char.isupper():
        new_text += chr((ord(char) + int(key) - A) % 26 + A)
    elif char.islower():
        new_text += chr((ord(char) + int(key) - a) % 26 + a)
    else:
        new_text += chr(ord(char))
print(new_text)
