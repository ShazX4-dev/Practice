''' Loop operators
(1) for
(2) break / else
(3) while
'''

print("===== for operator =====")
# iterable objects > string dict tuple list range map filter
text = "Mit"
numbs = [10, 7, 3, 4]
car_obj = dict(brand="ferrari", year=2016)
range_obj = range(5)

for letter in text:
    print(f"the letter: {letter}")

print("=============")

for number in numbs:
    print(f"the number: {number}")

print("="*5)

for x in range_obj:
    print(f"the element: {x}")

for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")

# print("="*10)
# for x in range(1, 20, 5):
#     # bu yerda 1ni 5ga qushib 6 keyin 6 ni 5ga qoshib 11 qaytaradi to 20magacham.
#     print(f"the x: {x}")


print("===== break / else =====")

print("="*10)
for x in range(1, 20, 5):
    # break amali toxtatib quyadi yani 10dan katta dedik bu yerda 11 10dan katta va shuning uvhun 16ni korsatmaydi chunki majburiy toxtash amalini qolaganmiz.
    print(f"the x: {x}")
    if x > 10:
        print("reached break")
        break
else:
    print("executed without any breaks")


print("===== while=====")

numb = 40
while numb > 0:
    numb -= 10
    print(f"the numb equals {numb}")

print("="*8)


count = 0
while True:
    count += 1
    x = int(input("find number"))

    if x == 41:
        print(f"You found number in {count} steps")
        break
    else:
        print("wrong Try again!")
