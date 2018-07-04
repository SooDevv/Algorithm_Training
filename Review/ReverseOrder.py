# 입력받는 형식 : enter
# 0 이 나오면 stop
# 1. 입력값 list에 append -> reverse

n = int(input())
rev = []

while True:
    if n == 0:
        break
    rev.append(n)
    n = int(input())

rev.reverse()
print(rev)

output =' '.join(map(str, rev))
print(output)



