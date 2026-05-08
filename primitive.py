print("======number=======")
#  in Java, variaable is a name of storage location
# in Python, variables is named reference!

count = 100
count_type = type(count)
# print("count:", count, count_type) bundan ko'ra qulayroq yozsak buladi bu xammasini bir joyda yozish imkonini beradi.
print(f"the count:{count} and type: {count_type}")


result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("======string=======")  # is also considered as string variables

# METHODS: upper() lower() title() find() replace()

course = "Ai Python FullStack"
result = type(course)
print(f"the result (1): {result}")

result = course.title()
print(f"the result (2): {result}")

result = course.upper()
print(f"the result (3):", {result})

result = course.replace("FullStack", "MasterClass")
print(f"the result (4):", {result})


print("======boolean=======")
# Function > type() input() bool() int() str()
y = input("Give your value for y:")
print("y:", y)

result = y.isnumeric()
print(f"the input value is numeric: {result}")


# TRUTHY vs FALSY value
# TRUTHY > True 100 -100 "MIT"
# FALSY > False 0 "" None

test_falsy = "" or False or None or 0
print("test_FALSY:", bool(test_falsy))

test_truthy = "MIT"
print("test_truthy:", bool(test_truthy))
