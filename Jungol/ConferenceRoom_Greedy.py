## input         ## output
# 6              # 3
# 1 1 10         # 2 5 4
# 2 5 6
# 3 13 15
# 4 14 17
# 5 8 14
# 6 3 12
#
import sys
read = sys.stdin.readline

def optimal_conference():
    n = int(input()) # 6
    arr = []
    for i in range(n):
        num, a, b = map(int, read().split())
        arr.append((b, a, num)) # 10, 1, 1

    arr.sort() # b 값을 sort 시키겠지

    time, cnt = 0, 0
    meet_list = []

    for b, a, num in arr:
        if a >= time:
            time = b
            meet_list.append(num)
            cnt += 1

    print(cnt);print(' '.join(map(str, meet_list)))

optimal_conference()



