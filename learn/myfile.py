def get():
    return "122223"


class Dog:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(self.name + " eat")



if __name__ == '__main__':
    print(123)
    print(get())
    dog1 = Dog("havana")
    dog1.eat()


