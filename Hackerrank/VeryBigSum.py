#5
#1000000001 (10개) , 1000000002 (10개), 1000000003
#1000000003
def bigsum(ar):
    sum = 0
    for i in range(len(ar)):
        sum += ar[i]
    return sum



if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = bigsum(ar)
    print(result)
