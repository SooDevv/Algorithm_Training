# 최대한 K-1을 만족
# K-1 이 짝수면, K-1 & K = K-1
# K-1 이 홀수면, K-1 || K = K-1

T = int(input())


def findmax(K, N):
    for k in range(K - 1, 0, -1):
        count = 0
        for a in range(N, 0, -1):
            if a & k == k:
                count += 1
                if count == 2:
                    return k
    return 0


for idx in range(T):
    N, K = map(int, input().split(' '))
    print(findmax(K, N))