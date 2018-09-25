# fibonacci - Memoization을 재귀적으로 구현


def fibonacci(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibonacci(n-1)+fibonacci(n-2))
    return memo[n]


if __name__ == '__main__':
    n = int(input())
    memo = [0, 1]
    res = fibonacci(n)
    print(res)