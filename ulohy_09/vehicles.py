class Vehicle:
    def __init__(self, name, distance):
        self.name = name
        try:
            float(distance)
            self.distance = distance
        except ValueError:
            print("Input must be a number.")

    def price_of_way(self, price_per_km):
        price = self.distance * price_per_km
        print(f"The journey cost is {price:.2f} Kč over "
              f"{self.distance} km by {self.name}.")


class Car(Vehicle):
    def price_of_way(self, consumption, price_of_fuel):
        try:
            float(consumption)
            float(price_of_fuel)
            super().price_of_way((consumption / 100) * price_of_fuel)
        except ValueError:
            print("Input must be a number.")


class Motorcycle(Vehicle):
    def price_of_way(self, consumption, price_of_fuel):
        try:
            float(consumption)
            float(price_of_fuel)
            super().price_of_way((consumption / 100) * price_of_fuel)
        except ValueError:
            print("Input must be a number.")


class Taxi(Vehicle):
    pass


class PublicTransport(Vehicle):
    def price_of_way(self, price_of_ticket):
        try:
            float(price_of_ticket)
            print(f"The journey cost is {price_of_ticket} Kč over "
                  f"{self.distance} km by {self.name}.")
        except ValueError:
            print("Input must be a number.")


octavia = Car("Škoda Octavia 1", 197)
octavia.price_of_way(7.5, 45)

ninja = Motorcycle("Kawasaki Ninja ZX-10R", 150)
ninja.price_of_way(5.9, 45)

taxi = Taxi("Bolt", 20)
taxi.price_of_way(35)

bus = PublicTransport("FlixBus", 225)
bus.price_of_way(349)

train = PublicTransport("ČD", 257)
train.price_of_way(375)
