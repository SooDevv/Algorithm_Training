def rotLeft(arr, d):
    # 1 2 3 4 5 , 4
    if len(arr) == 0:
        return arr
    rot = d % len(arr)
    return ' '.join(map(str,arr[rot:] + arr[:rot]))



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])
    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotLeft(arr, d)
    print(result)