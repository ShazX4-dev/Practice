def getHighestIndex(arr):
    # eng katta elementni topamiz
    max_value = max(arr)
    # birinchi uchragan indeksini qaytaramiz
    return arr.index(max_value)


print(getHighestIndex([5, 21, 12, 21, 8]))
