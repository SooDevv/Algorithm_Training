from collections import Counter

def solution(A):
    c = dict(Counter(map(int, A)))
    print(c)

    for k, v in c.items():
        if v % 2 != 0:
            return k


result = solution([9, 3, 9, 3, 9, 7, 9])
print(result)