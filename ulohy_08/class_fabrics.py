class Fabrics:
    def __init__(self, part, fabric_type):
        self.part = part.upper()
        self.fabric_type = fabric_type.upper()

    def price(self):
        """Ošetření, že bude zadáno pouze číslo."""
        while True:
            try:
                price = float(input(f"\n{self.part}: Kolik korun stojí bm látky? "))
                if price < 0:
                    print("Cena nemůže být záporné číslo.")
                    continue
            except ValueError:
                print("Cena není číslo nebo je desetinná čárka místo tečky.")
                continue
            else:
                return price

    def fabric_width(self):
        """Ošetření zadání šíře, nutné pro výpočet ceny za m2."""
        while True:
            try:
                width = int(input(f"{self.part}: Jaká je šíře látky v cm? ")) / 100
                if width <= 0:
                    print("Šíře nemůže být záporné číslo nebo 0.")
                    continue
            except ValueError:
                print("Šíře nebyla zadána správně. Zadávej v cm.")
                continue
            else:
                return width

    def fabric_price(self):
        """Výpočet ceny množství potřebného pro ušití"""
        if self.part == "PODŠÍVKA":
            used = 0.56
        elif self.part == "VNĚJŠÍ":
            used = 0.62
        else:
            print("Máme pouze části: 'podšívka' a 'vnější'")
            return 0

        part_price = self.price() / self.fabric_width() * used
        return part_price
