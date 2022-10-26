#a = 5
#b = 4

#def obsah_obdelniku(a, b):
#    return a * b

#print(f"Obsah obdélníku o stranách {a} a {b} cm je", obsah_obdelniku(a, b), "cm2.")

# Alternativa:
def obsah_obdelniku(a, b):
    if a <= 0 or b <= 0:
        print("Invalid number")
        return None
    return a * b

print(f"Obsah obdélníku o stranách 3 a 2 cm je", obsah_obdelniku(3, 2), "cm2.")