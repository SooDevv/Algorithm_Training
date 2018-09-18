# input :[3, 8, 9, 7, 6]
# input : 3
# output:[7, 6, 3, 8, 9]


def solution(A, K):
    if len(A) == 0:
        return A
    K = K % len(A)
    return A[-K:] + A[:-K]


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split(',')))
    k = int(input())

    result = solution(a, k)
    print(result)
