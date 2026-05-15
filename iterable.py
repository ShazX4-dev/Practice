print("======== Iterable objects & Range ====")
# Iterable objects > string dict tuple zip list range map filter

range_obj = range(3)
print("range_obj:", range_obj)

for letter in "MIT":
    print(f"the letter: {letter}")

for ele in range_obj:
    print(f"the element: {ele}")


print("======== DICTIONARY =======")
# Dictionary is Json Object!
person = {"name": "Tom", "age": 25, "single": False}
person_obj = dict(name="Tom", age=25, single=False)
print(f"the person: {person}")
print(f"the person_obj: {person_obj}")

# method: get() getni ishlatsak codelar crash bumaydi va dictni ichida hobby bumagani uchun none qiymat qaytadi
name = person_obj.get("name")
hobby = person_obj.get("hobby")
print(f"the name: {name}, hobby: {hobby}")

# del dict ichida keraksizini delete qiladi
del person_obj["single"]
for key in person_obj:
    print(f"the key: {key} => value {person_obj[key]}")
