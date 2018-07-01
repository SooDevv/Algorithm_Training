a = [[43, 26, 1],
     [2, 5, 8],
     [3, 7, 21]]

b = [[8, 6, 3, 6],
     [2, 3, 1, 1],
     [76, 4, 3, 1],
     [9, 4, 51, 22]]

def sum2D(list):
    total = 0
    for r in list:
        for c in r:
            total += c

    return total

result1 = sum2D(a)
result2 = sum2D(b)
print("result1", result1)
print("result2", result2)