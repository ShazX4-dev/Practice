def getHighestIndex(arr):
    # eng katta elementni topamiz
    max_value = max(arr)
    # birinchi uchragan indeksini qaytaramiz
    return arr.index(max_value)


print(getHighestIndex([5, 21, 12, 21, 8]))


def majorityElement(nums):
    # 1. Har bir elementni sanash uchun lug‘at (dict) yaratamiz
    count = {}

    # 2. Ro‘yxatdagi elementlarni aylantirib chiqamiz
    for num in nums:
        # Agar element lug‘atda bo‘lsa, qiymatini +1 qilamiz
        if num in count:
            count[num] += 1
        else:
            # Agar bo‘lmasa, uni 1 dan boshlab qo‘yamiz
            count[num] = 1

    # 3. Eng ko‘p takrorlangan elementni topamiz
    max_element = max(count, key=count.get)

    return max_element


# Sinab ko‘ramiz
print(majorityElement([1, 2, 3, 4, 5, 4, 3, 4]))  # natija: 4
