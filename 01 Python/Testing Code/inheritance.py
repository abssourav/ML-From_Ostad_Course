class Avengers:
    def __init__(self):
        self.avenger = "ironman"

    def fight(self):
        print(f"{self.avenger} is Fighting with Alien.")

class Ironman(Avengers):
    def passion(self):
        print(f"{self.avenger} is also a scientist.")


avenger1 = Ironman()
avenger1.fight()
avenger1.passion()