def maxNum(b):
    cnt = 0
    maxCnt = 0
    for i in b:
        # print(i)
        if i == '1':
            cnt += 1
            if cnt > maxCnt:
                maxCnt = cnt
        else:
            cnt = 0

    return maxCnt


if __name__ == '__main__':
    n = int(input())

    b = bin(n)
    res = maxNum(b[2:])
    print(res)