class Plastic_components:
    def __init__(self, type):
        self.type = type

    def component_price(self):
        """Ošetření, že bude zadáno pouze číslo."""
        while True:
            try:
                price = float(input(f"\nKolik korun stojí {self.type}? "))
                if price < 0:
                    print("Cena nemůže být záporné číslo.")
                    continue
            except ValueError:
                print("Cena nebyla zadána správně.")
                continue
            else:
                return price * 2
