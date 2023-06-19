import math

class Round:
    def __init__(self, radius: int) -> None:
        self.radius = radius
    
    def roundLength(self):
        return 2*math.pi*self.radius
    def square(self):
        return math.pi*self.radius**2

if __name__=="__main__":
    r = Round(10)
    print(r.roundLength())
    print(r.square())
