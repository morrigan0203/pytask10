

class Rectangle:

    def __init__(self, length: int, width=None) -> None:
        self.length = length
        if width == None:
            self.width = length
        else:
            self.width = width
    
    def perimetr(self):
        return 2*self.length+2*self.width
    def square(self):
        return self.length*self.width

if __name__=="__main__":
    r = Rectangle(10,20)
    print(r.perimetr())
    print(r.square())
    r2 = Rectangle(10)
    print(r2.perimetr())
    print(r2.square())

