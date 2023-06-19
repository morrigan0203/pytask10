

class Animal:

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

class Fish(Animal):

    def __init__(self, name: str, size: int, deepWater: bool) -> None:
        super().__init__(name, size)
        self.deepWater = deepWater

class Bird(Animal):

    def __init__(self, name: str, size: int, widthWings: int) -> None:
        super().__init__(name, size)
        self.widthWings = widthWings

class Zvery(Animal):

    def __init__(self, name: str, size: int, colorHair: str) -> None:
        super().__init__(name, size)
        self.colorHair = colorHair


if __name__=="__main__":
    f = Fish("Окунь", 15, False)
    b = Bird("Орел", 40, 150)
    z = Zvery("Волк", 100, "Серый")
    print(f.name,f.size,f.deepWater)
    print(b.name,b.size,b.widthWings)
    print(z.name,z.size,z.colorHair)

