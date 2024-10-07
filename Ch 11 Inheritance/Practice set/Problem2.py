class Animals:
    pass


class Pets(Animals):
    pass


class Dog(Pets):
    @staticmethod
    def bark():
        print("Bhaw Bhaw!")


d = Dog()

d.bark()
