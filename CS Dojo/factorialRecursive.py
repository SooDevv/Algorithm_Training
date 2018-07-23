#factorial = n! = n * (n-1)!
# hello world
import time
def factorial(idx):
    if idx == 0 or idx == 1:
        return 1
    else:
        return idx * factorial(idx - 1)


if __name__ == '__main__':
    start = time.time()
    result = factorial(int(input('factorial 구하기 프로그램! 숫자를 입력하세요: ')))
    print(result)
    endtime = time.time()

    print('timme', endtime-start)