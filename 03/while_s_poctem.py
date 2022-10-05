from random import randrange

counter = 0
while True:
    counter += 1
    if 13 == randrange(100):
        print("Super, to by šlo!")
        # print("trvalo to jenom " + str(counter) + "x")
        print("trvalo to jenom", str(counter), "x")
        break                           # ukončí cyklus
    print("Ne!")
