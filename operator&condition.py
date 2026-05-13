''' Operators & Conditions
(1) Operators
(2) Condition
(3) Logical operators
'''

print("===== Operators =====")
# + - > >= < <= * /   // $ += **

a = 19
b = 5
print(a / b)
result = a // b  # bu amal 19 ni 5 ga bulgandagi butun soni kursatadi (3)
left = a % b  # bu esa 19 ni 5 ga bulganda qolgan qoldiqni kursatadi (4)
print(f"the result: {result} and left: {left}")


# a = a + 100
a += 100
print("a:", a)

print("b**2", b**2)
print("b**3", b**3)

print("="*5)  # ("====="*5) xattoki stringlarnixam kopaytirib beradi

c = dict(name="Shoxa", age=35)
d = dict(name="Tom", age=25)
e = c
print("c==d", c == d)  # only value yani faqat qiymat


data = c is d
print("c is e", c is e)


print("===== Condition =====")

x = 20

if x > 50:
    print("case A")
elif x > 10:
    print("case B")
else:
    print("Case C")


print("---------------")

age = 20
# person = None

# if age > 16:
#     person = "Adult"
# else:
#     person = "child"

# print("person:", person)


# TERNARY
person = "adult" if age > 18 else "minor"
print("person:", person)

print("---------")

is_student = True
is_admin = False
is_guest = True
is_parent = True

if not is_student:
    print("Welcome here, do u want to be a student?")
elif is_admin:
    print("Please go to this office")
# or true qiymatgacha uqiydi agar chap taraf true bulsa qolganlariga qaramaydi.
elif is_guest or is_parent:
    print("waiting room is over here")
else:
    print("other case")
