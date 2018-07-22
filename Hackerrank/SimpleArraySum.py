
def sumArray(c, arr):
    sum = 0
    for i in range(c):
        sum += arr[i]
    return sum


if __name__ == '__main__':
    c = int(input())

    arr_values = list(map(int, input().rstrip().split()))

    result = sumArray(c, arr_values)

    print(result)