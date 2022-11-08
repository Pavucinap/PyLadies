# Napiš funkci vyhodnot, která dostane řetězec s herním polem 1-D piškvorek 
# a vrátí jednoznakový řetězec podle stavu hry:
# "x" – Vyhrál hráč s křížky (pole obsahuje xxx)
# "o" – Vyhrál hráč s kolečky (pole obsahuje ooo)
# "!" – Remíza (pole neobsahuje -, a nikdo nevyhrál)
# "-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)

def vyhodnot(pole):
    if "xxx" in pole:
        result = "x"
        # Vyhrál hráč s křížky.
    elif "ooo" in pole:
        result = "o"
        # Vyhrál hráč s kolečky.
    elif "-" not in pole:
        result = "!"
        # Remíza
    else:
        result = "-"
        # Hra pokračuje
    
    return result

pole = "xox-xooo"

print(vyhodnot(pole))
