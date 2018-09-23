# timeout ㅠㅠ
# def minimumSwaps(arr):
#     cnt = 0
#
#     for i in range(len(arr)):
#         minValue = min(arr[i:])  # arr 에서 가장 작은 값
#         idx = arr.index(minValue)  # 가장 작은 값의 index
#         if idx != i:
#             arr[i], arr[idx] = arr[idx], arr[i]
#             cnt += 1
#         else:
#             continue
#
#     return cnt

def minimumSwaps(arr, n):
    count = 0
    for i in range(n-1):#0, 1 ,2
        while (arr[i]!=i+1):
            key = arr[i] -1
            arr[i], arr[key] = arr[key], arr[i]
            count += 1
    return count


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr,n)
    print(res)