def luckBalance(k, contests):
    # imp = [val_imp[0] for val_imp in contests if val_imp[1] == 1]
    # unimp = [val_imp[0] for val_imp in contests if val_imp[1] == 0]
    #
    # imp.sort() # 1, 2, 5, 8
    #
    # arr = imp[-k:] + unimp # 1, 2, 5, 8 // 10, 5
    # arr_unimp = imp[:(len(imp)-k)]
    #
    # # print(arr_unimp)
    # return sum(arr) - sum(arr_unimp)


    imp = []
    imp_sum = 0
    unimp_sum = 0

    for val_imp in contests:
        if val_imp[1] == 1:
            imp.append(val_imp[0])
            imp_sum += val_imp[0]
        else:
            unimp_sum += val_imp[0]

    imp.sort()

    for i in range(len(imp)-k):
        imp_sum -= 2 * imp.pop(0)


    return imp_sum + unimp_sum




if __name__ == '__main__':
    # n, k(적어도k개 포함)
    # L, T
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    contensts = []

    for _ in range(n):
        contensts.append(list(map(int, input().rstrip().split())))

    print(contensts)
    result = luckBalance(k, contensts)

    print(result)