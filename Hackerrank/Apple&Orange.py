# # s,t = 7 11
# # a,b = 5 15
# # count = 3 2
# # apples = -2 2 1
# # oranges = 5 -6

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # 집 7, 8, 9, 10, 11
    # house = [i for i in range(s, t+1)]

    apples = [i+a for i in apples]
    oranges= [i+b for i in oranges]
    print('apple위치: {0}, oranges위치:{1}'.format(apples, oranges))

    countA = sum([range(s,t+1).count(i) for i in apples])
    countO = sum([range(s,t+1).count(i) for i in oranges])

    return countA, countO

if __name__ == '__main__':

    #집
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    # print('s,t = {0},{1}'.format(s,t))
    #사과 오렌지 나무
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    # print('a,b = {0},{1}'.format(a,b))

    #갯수
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    # print('n,m = {0},{1}'.format(n,m))

    #사과 좌표
    apples = list(map(int, input().rstrip().split()))
    # print('apples = {0}'.format(apples))

    #오렌지 좌표
    oranges = list(map(int, input().rstrip().split()))
    # print('oranges = {0}'.format(oranges))


    result = countApplesAndOranges(s, t, a, b, apples, oranges)
    for i in result:
        print(i)