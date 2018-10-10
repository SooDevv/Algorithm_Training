def countSwaps(a):
    cnt = 0
    for size in reversed(range(len(a))):
        for i in range(size):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1], a[i]
                cnt += 1
    print('Array is sorted in {} swaps.'.format(cnt))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)