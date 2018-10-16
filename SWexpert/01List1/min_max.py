if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        diff = max(arr) - min(arr)
        print(diff)