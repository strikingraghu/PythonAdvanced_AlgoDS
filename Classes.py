"""

    Object-oriented programming (OOP) is a programming paradigm that uses objects and their interactions to
    design applications and computer programs. There are some basic programming concepts in OOP:
        Abstraction
        Polymorphism
        Encapsulation
        Inheritance
    The abstraction is simplifying complex reality by modeling classes appropriate to the problem.
    The polymorphism is the process of using an operator or function in different ways for different data input.
    The encapsulation hides the implementation details of a class from other objects.
    The inheritance is a way to form new classes using classes that have already been defined.

"""
# Code for some sample classes, methods and instance methods
# generic oop's code


class Parrot:

    # class attribute
    species = 'bird'

    # instance attribute
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # instance methods
    def sing(self, language):
        print("Parrot sings in " + language)
        return language

parrot1 = Parrot('Tobi', 'Green')
parrot2 = Parrot('Helm', 'Black')

print("Accessing First Parrot Info :", parrot1.species, parrot1.name, parrot1.color, parrot1.sing('English'))
print("Accessing Second Parrot Info :", parrot2.species, parrot2.name, parrot2.color, parrot2.sing('Hindi'))
print('-----------------------')

# inheritance


class Bird:

    def __init__(self):
        print("Bird is ready")

    def who_is_this(self):
        print("Bird")

    def swim(self):
        print("Swim Faster")


class Penguin(Bird):

    def __init__(self):
        super().__init__()  # calling super method
        print("Penguin is ready")

    def who_is_this(self):
        print("Penguin")

    def swim(self):
        print("I can't swim faster!")


# instantiation
peggy = Penguin()
peggy.who_is_this()
peggy.swim()
print('-----------------------')


# abstraction


class Vehicle:

    def __init__(self, engine_type, color):
        self._engine_type = engine_type
        self._color = color
        print("Vehicle Details =", self, engine_type, color)

    base_price = 0.0

    def number_of_wheels(self, number):
        if number == 4:
            print("It's a 4 wheeler")
        elif number == 2:
            print("It's a 2 wheeler")
        else:
            print("You don't have proper vehicle")


class Bike(Vehicle):

    def bike_price(self):
        bike_price = 55000
        return bike_price


class Car(Vehicle):

    def car_price(self):
        car_price = 355000
        return car_price

# instantiation
pulsar = Bike('Petrol', 'Black')
swift = Car('Diesel', 'Red')
pulsar.number_of_wheels(2)
print(pulsar.bike_price())

swift.number_of_wheels(4)
print(swift.car_price())

print("--------------------------")

# encapsulation logic


class Computer:

    def __init__(self):
        print("Inside Computer Class")
        self._brand = 'Lenovo'

    def model(self):
        model = 'T440S'

    def comp_price(self, price):
        comp_price = 40000
        if comp_price > 40000:
            print("You are paying more!")
        elif comp_price < 40000:
            print("You are paying less")

# instantiation
laptop = Computer()
laptop.comp_price(35000)
print("--------------------------")


# polymorphism


class Dog:

    def __init__(self):
        print("Inside Dog Class")

    def run(self):
        print("Dogs can run!")


class Labrador:

    def __init__(self):
        print("Inside Labrador Class")

    def run(self):
        print("Labrador can also run!")

# common interface


def lets_test_running(any_dog):
    any_dog.run()

# instantiation
puppy01 = Dog()
puppy02 = Labrador()
puppy01.run()
puppy02.run()

lets_test_running(puppy01)
lets_test_running(puppy02)
print("--------------------------")
