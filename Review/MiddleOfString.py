# String 의 갯수
# 홀수 -> 가운데 값 1개
# apple -> 2 : 3
# 짝수 -> 가운데 값 2개
# nano -> 1 : 3hehhh
# nano[1:3]

str = input()
def middle(str):
    return str[(len(str) - 1) // 2 : (len(str) // 2) + 1]

result = middle(str)
print("sol1 :",result)

## solution 2
def middle2(str):
    if len(str) % 2 != 0:
        return str[len(str) // 2]
    else:
        return str[(len(str)-1) // 2 : (len(str) // 2 )+1]

print("sol2 :", middle2(str))