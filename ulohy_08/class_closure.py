class Closure:
    def __init__(self, product):
        self.product = product

    def closure_price(self):
        """Volba, zda se zapínáním nebo bez, podle toho cena"""
        while True:
            answer = input(f"Bude mít {self.product} zapínání? (a/n) ")
            if answer.lower() in ["ano", "a"]:
                return self.price()
            elif answer.lower() in ["ne", "n"]:
                break
            else:
                print("Toto není správná odpověď.")
        return 0

    def price(self):
        """Ošetření, že bude zadáno pouze číslo."""
        while True:
            try:
                price = float(input("Kolik zvolené zapínání stojí? "))
                if price < 0:
                    print("Cena nemůže být záporné číslo.")
                    continue
            except ValueError:
                print("Cena nebyla zadána správně.")
                continue
            else:
                return price
