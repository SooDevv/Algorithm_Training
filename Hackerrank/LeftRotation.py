## input : 5 4 / 1 2 3 4 5
## output : 5 4 3 2 1 (str)

n, d = map(int, input().split())
arr = list(map(int, input().rstrip().split()))

# arr = []
# for i in range(1, n+1):
#     arr.append(i)
print(arr)

for i in range(1, d+1):
    first = arr[0]
    arr.remove(arr[0])
    arr.append(first)

sep = " "
result = sep.join(map(str, arr))
print(result)