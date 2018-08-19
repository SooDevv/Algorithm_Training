# <<input>>                 # <<output>>
# 4                         # 2
# -15 5
# -10 36
# 10 73
# 27 44

def getRefrigerator():
    n = int(input())
    arr = []

    for i in range(n):
        min, max = map(int, input().split())
        arr.append((min, max))


    arr.sort()

    cnt = 0
    temp = 0 # 냉장고 번호
    refri_size = []

    for min, max in arr:

        if min not in refri_size:
            refri_size = [i for i in range(min,max+1)]
            cnt += 1

    return cnt


result = getRefrigerator()
print(result)