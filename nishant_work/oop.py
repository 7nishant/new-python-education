#What is OOP? What are the OOP concept for python? explain with programming.
# Object-oriented Programming, or OOP for short, is a programming paradigm which provides a means of structuring
# programs so that properties and behaviors are bundled into individual objects. Python is a great programming
# language that supports OOP. You will use it to define a class with attributes and methods, which you will then call.
# Python offers a number of benefits compared to other programming languages like Java, C++ or R. It's a dynamic
# language, with high-level data types. This means that development happens much faster than with Java or C++. It does
# not require the programmer to declare types of variables and arguments. This also makes Python easier to understand
# and learn for beginners, its code being more readable and intuitive.

#Inheritance :-A process of using details from a new class without modifying existing class.Inheritance is a way of
# creating new class for using details of existing class without modifying it. The newly formed class is a derived class
# (or child class). Similarly, the existing class is a base class (or parent class).

class Bird:

    def __init__(self):
        print("Bird is ready")

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready")
peggy = Penguin()
#Encapsulation :-Hiding the private details of a class from other objects. Using OOP in Python, we can restrict access
# to methods and variables. This prevent data from direct modification which is called encapsulation. In Python, we
# denote private attribute using underscore as prefix i.e single “ _ “ or double “ __“.

class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()
# Polymorphism :-A concept of using common operation in different ways for different data input.Polymorphism is an
# ability (in OOP) to use common interface for multiple form (data types).

class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class fish:

    def fly(self):
        print("fish can't fly")

    def swim(self):
        print("fish can swim")


def flying_test(bird):
    bird.fly()




blu = Parrot()
peggy = fish()


flying_test(blu)
flying_test(peggy)