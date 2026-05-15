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
