## input
## 4
## 1 2 5 4
## output
## 4 5 2 1

def reverseArray(a):
    a.reverse()
    return a

n = int(input())
##rstrip : 오른쪽 공백 제거
arr = list(map(int, input().rstrip().split()))

res = reverseArray(arr)

##배열을 문자열로 바꾸는 방법
sep = " "
output = sep.join(map(str, res))
print(output)





