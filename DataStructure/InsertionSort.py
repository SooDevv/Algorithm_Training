# list 의 index 1 부터 비교 시작
# 찾는 위치 idx
# 찾아야할 값 tmp
# 비교해야될 위치 i

def insertionSort(arr):
    for idx in range(1, len(arr)):
        tmp = arr[idx]
        i = idx
        while i>0 and arr[i-1] > tmp:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = tmp
    return arr


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    result = insertionSort(arr)
    print(result)