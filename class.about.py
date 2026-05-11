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
