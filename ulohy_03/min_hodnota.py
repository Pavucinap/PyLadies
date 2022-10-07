min = float('inf')
for _ in range(5):
    while True:
        n = str(input("Zadej číslo: "))
        if n.isdigit():
            m = int(n)
            if m < min:
                min = m
            break
        print("Toto není správné zadání!")

print("Nejmenší zadané číslo je:", min)