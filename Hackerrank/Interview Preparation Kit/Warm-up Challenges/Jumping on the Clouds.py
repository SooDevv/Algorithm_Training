# 기본 i --> i+2
# i+2 가 1(thundercloud)이면, i+1

n = int(input())
i = 0
cloud = list(map(int, input().split()))
jump = 0

while i < n-1:
    if i+2 < n and cloud[i+2] == 0:
        i = i+2
        jump += 1
    else:
        i = i+1
        jump += 1

print(jump)