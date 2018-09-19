# 원래 생각한 방식 : CNN의 filter처럼 벡터의 곱을 이용하여 구하려 했음
# 그냥 배열의 위치만 따서 바로바로 합하고 sorting 하는게 더 효율적 ^^

def hourglassSum(arr):
    subglass = []

    ## 총 4x4가 나오므로 iteration:4
    for i in range(4):
        for j in range(4):
            li = arr[i][j] + arr[i][j+1] + arr[i][j+2] \
                    + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] \
                    + arr[i+2][j+2]
            subglass.append(li)

    subglass.sort()

    return subglass[15]



if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))


    result = hourglassSum(arr)
    print(result)