def main():
    x, y = map(int, input().rstrip().split())
    data = [[0]*y for _ in range(x)]

    for i in range(x):
        tmp = input()
        for j in range(y):
            data[i][j] = int(tmp[j])
    # print(data)

    visit = [[0]*y for _ in range(x)]

    direction = [(0,1),(0,-1),(1,0),(-1,0)]

    # bfs
    arr = []
    arr.append((0,0))
    visit[0][0] = 1
    while arr:
        # queue니깐 pop(0)
        a, b = arr.pop(0)
        
        # 도착 지점에 도착시
        if a == x-1 and b == y-1:
            print(visit[a][b])
            break

        for dir in direction:
            ax = a + dir[0]
            ay = b + dir[1]
            if ax>=0 and ax<x and ay>=0 and ay<y: #틀 안벗어나는 조건
                if visit[ax][ay]==0 and data[ax][ay]==1: #방문하지 않은 곳이고, 갈 수 있는 조건
                    visit[ax][ay] = visit[a][b]+1
                    arr.append((ax,ay))



if __name__ == '__main__':
    main()