''' OBJECTS
(1) What is object
(2) Iterable objects & RANGE
(3) DICTIONARY
(4) ERROR HANDLING SYTEM
'''
import array  # package/module
import math  # from math ceil deb yaxlit ceil methodini qulga olsa buladi
print("====== What is object =======")
# an object has state and method properties.
# everything is object in python!

print(type("Hello World!"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP 4 CONCEPTS > Abstraction | Encapsulation | Inheritence | Polimorphism
result1 = math.ceil(97.7)  # Call
print("result:", result1)


print("======= Error handling system =========")
car_dict = dict(name="Tayota", year=2026, electric=True)

try:
    result = car_dict["year"]
    print("result:", result)


except KeyError as err:
    print("No origin state property founds:", err)
else:
    print("executed successfully withour errors")
finally:
    print("final closing logic")
