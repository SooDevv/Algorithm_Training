def bigSorting(unsorted):
    unsorted.sort()
    return unsorted


if __name__ == '__main__':
    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(int(unsorted_item))

    result = bigSorting(unsorted)
    print('\n'.join(map(str, result)))
