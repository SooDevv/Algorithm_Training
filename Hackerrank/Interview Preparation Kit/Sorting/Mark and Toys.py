def maximumToys(prices, money):
    prices.sort()
    cnt = 0

    for i in prices:
        if money-i > 0:
            money -= i
            cnt += 1
    return cnt


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    prices = list(map(int, input().rstrip().split()))

    res = maximumToys(prices, m)
    print(res)


