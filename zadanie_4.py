import zadanie_3 as z3

class Emploee(z3.Person):

    def __init__(self, name: str, surname: str, age: int, id: int) -> None:
        super().__init__(name, surname, age)
        self.__id = id
    
    def level(self):
        return self.__id%7
    def id(self):
        return self.__id

if __name__=="__main__":
    e = Emploee("Vasya", "Petrov", 20, 123456)
    print(e.fullName(), e.age(), e.id(), e.level())