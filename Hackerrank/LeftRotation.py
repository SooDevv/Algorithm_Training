n, d = map(int, input().split())

arr = []
for i in range(1, n+1):
    arr.append(i)
print(arr)

for i in range(1, d+1):
    first = arr[0]
    arr.remove(arr[0])
    arr.append(arr[0])

print(arr)