# 멤버쉽 연산자 사용해 볼 것
# in, not in

s = input()

check = []
while True:
    if s in check:
        break
    print(s)
    check.append(s)
    s = input()
