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
