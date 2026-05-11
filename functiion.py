''' Function
(1) define vs call
(2) parametr vs argument
(3) keyword & dafault argument
(4) scope 
'''

print("======= Define vs Call ===========")

# build in function > print() typer()
# function - reusable block of code
# instead of block {} in JAVA, Python uses indentation


# DEFINE - build
def greet(a):  # a parametr
    print(f"Hello qondaysen, {a}")


def greeting(b):
    print("greetin ishga tushdi")
    return f"hi{b}"


# CALL - execute
result1 = greet('Tom')  # Tom va Shoxa argument
print("result1:", result1)

result2 = greeting('Shoxa')
print("result2:", result2)


print("======= Keyword $ default arguments ======")
# DEFINE


# bu yerda age ga bargument bersak callda yozmasak xam default argument buladi
def give_greet(name, age=32):
    print("give_greet is executed")
    return f"hi {name}, you are {age} rears old"


# keyword argument bu aniqlik qilib yozish yani name age id larini yozib argument yozish.
# CALL
result3 = give_greet(name="Tom", age="32")
print("result3:", result3)

result4 = give_greet("John")
print("result4:", result4)
