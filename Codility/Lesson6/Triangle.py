def solution(arr):
    i = 0
    while i < len(arr)-2:
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if arr[j]+arr[k]>arr[i] and arr[i]+arr[j]>arr[k] and arr[i]+arr[k]>arr[j]:
                    return 1
                else:
                    continue
        i += 1
    return 0


if __name__ == '__main__':
    res = solution([10,50,5,1])
    # res = solution([10,2,5,1,8,20])
    # res = solution([5,3,3])
    print(res)