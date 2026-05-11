''' CLASS
(1)What is Class
(2) Ordinary vs static properties
(3) Special methods
'''

print("====== What is Class =======")
# class -blueprint object yasovchi shablon
# Structure > state constructor method


class Person():
    # state
    message = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method

    def introduce(self):
        print(f"{self.name} says: How do u do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}!")

    @classmethod
    def explain(cls):
        print("static method property executed")


person1 = Person("Honor", 24)
person2 = Person("Shoxa", 32)
person3 = Person("Baxa", 30)


# ordinary method
person1.introduce()
person2.say_age()


print("====== Ordinary vs static properties  =======")


# static state
new_message = Person.message
print("new_message:", new_message)

# Static  Method
Person.explain()

print("====== Special methods  =======")

# Pyton's most used special methods are below
# __init__, __new__, __str__, __call__ __getitem__ __eq__ __len__ ...add()


class car():
    # state
    description = "This class makes cars"

    # constructor
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # method
    def start_engine(self):
        print(f"the{self.name} started engine")

    def stop_engine(self):
        print(f"the{self.name} stopped engine")

    def __str__(self):
        return f"thecar.name {self.name} was produced in {self.year} year"

    def __call__(self,):
        print("object called as function")


my_car = car("Ferrari", 2026)
my_car.start_engine()
my_car.stop_engine()

print("---------")
your_car = car("Tayota", 2026)
print(your_car)
your_car()  # calling look like a function
