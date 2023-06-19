

class Person:

    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name
        self.surname = surname
        self.__age = age
    
    def birthday(self):
        self.__age = self.__age + 1
    
    def age(self):
        return self.__age
    
    def fullName(self):
        return self.name + " " + self.surname


if __name__=="__main__":
    p = Person("Ivan","Pupkin",30)
    print(p.fullName(), p.age())
    p.birthday()
    print(p.fullName(), p.age())


