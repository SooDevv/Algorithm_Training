import time


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        return result

if __name__ == '__main__':
    start = time.time()
    n = int(input())
    print(fibonacci(n))

    end = time.time()

    print('time', end - start)