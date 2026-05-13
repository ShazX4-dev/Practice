''' 
(1)   Class deep diving
(2) Encapsulation
(3) Inheritance
(4) Polimorphism
'''


print("===== Polimorphism ======")


class Animal:

    description = "The class creates animals"

    def __init__(self, voice):
        self.voice = voice

    def make_voice(self):
        print(f"this animal can make voice: {self.voice}")


class Dog(Animal):

    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("yes I can protect you!")

    def make_voice(self):
        print(f"this {self.name} says {self.sound}")


dog = Dog("Rex", "wow", True)

dog.introduce()
dog.protect()
dog.make_voice()

print("=============")
# dog > dog instanse > Animal > object
a = isinstance(dog, Dog)
print(f"The result:", {a})
