class Cats:
    def __init__(self, name):
        self.name = name
        self.lives = 9

    def meow(self):
        if self.is_alive:
            print(f"{self.name}: Meow!")

    def is_alive(self):
        return self.lives > 0

    def lose_life(self):
        if self.is_alive():
            self.lives -= 1
            print(f"{self.name} lost life.")

    def eat(self, food):
        if self.is_alive():
            if food == "fish" and self.lives < 9:
                self.lives += 1
                print(f"{self.name} eats {food} and gets a live")
            else:
                print(f"{self.name} eats {food}, I like {food}.")




micka = Cats("Micka")
mourek = Cats("Mourek")

micka.lose_life()
micka.eat("meat")
print(f"{micka.name} has {micka.lives} lives")

mourek.lose_life()
mourek.eat("fish")
print(f"{mourek.name} has {mourek.lives} lives")
mourek.eat("fish")
print(f"{mourek.name} has {mourek.lives} lives")
