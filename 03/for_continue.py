print("continue:")
for i in range(20):
    if i > 9 and i < 15:
        continue
    print(i)

print()

print("break:")
for i in range(15):
    if i > 7 and i < 12:
        break               # ukončí po dosažení konce první podmínky
    print(i)