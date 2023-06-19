import zadanie_5_6 as z56


class Factory:

    def instance(self, clasName: str, *args):
        if clasName == "Fish":
            return self.__instanceFish(*args)
        elif clasName == "Bird":
            return self.__instanceBird(*args)
        elif clasName == "Zvery":
            return self.__instanceZvery(*args)
        else:
            raise ValueError(clasName)
    
    def __instanceFish(self, *args):
        return z56.Fish(*args)
    def __instanceBird(self, *args):
        return z56.Bird(*args)
    def __instanceZvery(self, *args):
        return z56.Zvery(*args)

if __name__=="__main__":
    f = Factory()
    print(f.instance("Fish","Окунь",10,False).name)

