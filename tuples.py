''' TUPLE
(1) What is tuple: typle vs list
(2) Unpacking arguments
(3) Zip
'''
print("====== What is tuple: typle vs list ============")

# JAVA , PHP , NodeJs dagi array PYTHONDA list bo'ladi.

# list qurish (1) literal (2) constructor(classlar orqali)

# literal
numbs = [3, 5, 1, 2]


# constructor
letters = list("Hello World")

fruits = ["apple", "lemon", "banana", "kivi"]
print("before fruits:", fruits)

# shu orqali berilgan qiymatlarimizni bemalol almashtirsak bo'ladi.
fruits[2] = "melon"
print("after fruits:", fruits)


# tuple xech qachon berilgan qiymatini uzgartirmaydi
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)


print("====== Unpacking arguments =======")

groups = ["Mit", "Flexy", "Devex", "Mg"]
(x, y, z, *z) = groups
print(f"the x: {x} and y: {y}")
# *z deb yozsak x bilan y ni uzini alohida qiymatlarini oladi va qolganlarini bita listga taxlaydi
print("z:", z)


# *args > tuple
def calculate(*args):
    print("*args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


# CALL
calculate(1, 7, 2, 3)


# **kvargs > dictionary
def introduce(**kwargs):
    print(f"the type (**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old!")
    pass


# Call
introduce(name="Justin", age=28)
print("="*50)


def greeting(*args, **kwargs):
    print("*args >", args)
    print("**kwargs >", kwargs)

    # CALL
greeting("hi", True, 10, name="Tom", age=22)
