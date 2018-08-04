# 4
# 6
# 1 4 2 3 5 6

def introTutorial(v, arr):
    for i in range(len(arr)):
        if v == arr[i]:
            return i




if __name__ == '__main__':
    v = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(v, arr)

    print(result)