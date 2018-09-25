def factorial(n):
    # 3! = 3*2*1
    if n == 1:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    n = int(input())

    res = factorial(n)
    print(res)