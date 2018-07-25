def compare(a, b):
    aWin = 0
    bWin = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            aWin += 1
        elif a[i] == b[i]:
            pass
        elif a[i] < b[i]:
            bWin += 1
    return [aWin, bWin]

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compare(a, b)
    print(result)
