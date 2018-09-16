def sockMerchant(n, ar):
# n = 9, ar = list
# sort --> 10 10 10 10 20 20 20 30 50
# inx       0  1  2  3 4  5  6  7  8
# cnt = pair of socks
# tmp = list[0]
    tmp = ar[0]
    cnt = 0
    i = 1
    while i<n:
        try:
            if tmp == ar[i]:
                cnt += 1
                tmp = ar[i+1]
                i += 2
            else:
                tmp = ar[i]
                i += 1
        except IndexError:
            i += 1

    return cnt

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))
    ar.sort()

    result = sockMerchant(n, ar)
    print(result)