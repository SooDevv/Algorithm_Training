# 인접 행렬을 이용한 DFS/BFS 알고리즘
# 노드에 비해 간선이 많으며, 두 노드간의 관계를 알고 싶을 때 사용

def dfs(i):
    dfs_arr.append(i)
    visit.add(i)
    j = 1

    while j<n:
        j += 1
        if N[i][j] == 1 and j not in visit:
            dfs(j)

    return ' '.join(map(str, dfs_arr))

def bfs(i):
    que.insert(0, i)
    while len(que) != 0:
        x = que.pop(0)
        visit.add(x)
        # print(x)
        bfs_arr.append(x)
        i = 0
        while i <n+1:
            if N[x][i] == 1 and i not in visit:
                visit.add(i)
                que.append(i)
            i += 1

    return ' '.join(map(str, bfs_arr))


if __name__ == '__main__':
    n, e, v = map(int, input().split())

    N = [[0]*(n+1) for _ in range(n+1)]

    # visit = [0 for _ in range(n+1)]
    visit = set()
    for i in range(e): # 간선 수
        i, j = map(int, input().split())
        N[i][j] = N[j][i] = 1 # 양방향

    # DFS
    dfs_arr = []
    res = dfs(v)
    print(res)

    #BFS
    visit = set()
    que = []
    bfs_arr = []
    res = bfs(v)
    print(res)