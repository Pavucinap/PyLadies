class Straps:
    def __init__(self, material):
        self.material = material

    def strap_price(self):
        """Ošetření, že bude zadáno pouze číslo."""
        while True:
            try:
                price = float(input("\nKolik korun stojí metr popruhu? "))
                if price < 0:
                    print("Cena nemůže být záporné číslo.")
                    continue
            except ValueError:
                print("Cena nebyla zadána správně.")
                continue
            else:
                return price * 2.7
