import util


class Vehicle:
    def __init__(self, brand, type, color):
        self.brand = brand
        self.type = type
        self.color = color
        self.rent_per_day = ""
        print(f"It is {self.brand} {self.type} and its color is {self.color}.")

    def show_vehicle(self):
        show = "You approach the vehicle. " \
            + self.open_door() \
            + self.sit_and_switch_engine() \
            + self.inspect_vehicle() \
            + self.honk()
        return show

    def open_door(self):
        return f"You open a door.\n"

    def sit_and_switch_engine(self):
        return f"You sit and switch engine.\n"

    def inspect_vehicle(self):
        return f"You inspect lights, liquids and wipers.\n"

    def honk(self):
        return f"You honk. It sounds:'Meeeep, meeeeep'."

    def set_rent_per_day(self, rent_per_day):
        self.rent_per_day = rent_per_day

    def rent_price(self, days):
        days = util.validate_days(days)

        if 0 < days <= 7:
            return self.rent_per_day * days
        elif 7 < days <= 14:
            return self.rent_per_day * days * 0.9
        elif 14 < days <= 21:
            return self.rent_per_day * days * 0.8
        else:
            return self.rent_per_day * days * 0.7

    def rent_price_text(self, days):
        print(f"Rent of {self.brand} {self.type} is "
              f"{self.rent_price(days):.0f} Kč for {days} days.\n\n")


class Car(Vehicle):
    def __init__(self, brand, type, color, number_of_door, number_of_seats, fuel):
        self.number_of_door = number_of_door
        self.number_of_seats = number_of_seats
        self.fuel = fuel
        print("This vehicle is car.")
        super().__init__(brand, type, color)
        print(f"It has {self.number_of_door} door and "
              f"{self.number_of_seats} seats.")
        print(f"It runs on {self.fuel}.")
        super().set_rent_per_day(600)


class Motorcycle(Vehicle):
    def __init__(self, brand, type, color, fuel):
        self.fuel = fuel
        print("This vehicle is motorcycle.")
        super().__init__(brand, type, color)
        print(f"It runs on {self.fuel}.")
        super().set_rent_per_day(3500)

    def show_vehicle(self):
        show = "You approach the vehicle. " \
            + self.sit_and_switch_engine() \
            + self.inspect_vehicle() \
            + self.honk()
        return show

    def inspect_vehicle(self):
        return f"You inspect lights and liquids.\n"


class Truck(Vehicle):
    def __init__(self, brand, type, color, fuel):
        self.fuel = fuel
        super().__init__(brand, type, color)
        super().set_rent_per_day(4000)

    def about_vehicle(self):
        print("This vehicle is car.")
        super().about_vehicle()
        print(f"It has 2 doors and 2 seats.")
        print(f"It runs on {self.fuel}.")

    def sit_and_switch_engine(self):
        return f"You climb into cab, sit and switch engine.\n"

    def honk(self):
        return f"You honk. It goes:'Traaaaa, traaaaaaaaaaaa.'"


octavia = Car("Škoda", "Octavia 1", "silver", "5", "5", "gasoline")
print(octavia.show_vehicle())
octavia.rent_price_text(5)

kawasaki = Motorcycle("Kawasaki", "Ninja", "green", "gasoline")
print(kawasaki.show_vehicle())
kawasaki.rent_price_text(10)

man = Truck("MAN", "TGX4X4", "white", "diesel")
print(man.show_vehicle())
man.rent_price_text(25)
