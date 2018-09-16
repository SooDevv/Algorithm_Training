from collections import Counter

n = int(input())

c = Counter(map(int, input().rstrip().split()))
ans = 0

for i in c:
    ans += c[i] // 2

print(ans)