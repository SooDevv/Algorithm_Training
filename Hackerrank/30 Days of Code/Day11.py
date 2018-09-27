if __name__ == '__main__':
    # 2차원 배열 입력받음
    arr = []

    for _ in range(6):
        # 한줄 씩 총 6줄 입력 받음
        arr.append(list(map(int, input().rstrip().split())))

    maxNum = []

    for i in range(4):
        for j in range(4):
            cnt = arr[i][j]+arr[i][j+1]+arr[i][j+2] \
            + arr[i+1][j+1] \
            + arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            maxNum.append(cnt)

    maxNum.sort()
    print(maxNum[15])
