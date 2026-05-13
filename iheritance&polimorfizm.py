''' 
(1)   Class deep diving
(2) Encapsulation
(3) Inheritance
(4) Polimorphism
'''


print("===== INHERITANCE ======")
# PARENT > CHILD
# parent uzini faqat public & protected propertylarini(state, method) farzandiga utgazadi. private utmaydi


class Animal:  # father
    # state
    description = "The class creates animals"

    # constructor
    def __init__(self, voice):
        self.voice = voice

    # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("yes I can protect you!")


dog = Dog("Rex", "wow", True)

dog.introduce()
dog.protect()
