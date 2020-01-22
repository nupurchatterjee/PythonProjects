class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * self.pi

    def get_circum(self):
        return self.radius * self.pi * 2


my_circle = Circle(10)
value = my_circle.get_circum()
print(my_circle.pi)
print(value)


class Animal:

    def __init__(self):
        print("Animal Created")

    def who_am_I(self):
        print("Animal")

    def _eat(self):
        print("Im eating")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog created")


my_dog = Dog()
my_dog.who_am_I()
my_dog._eat()

