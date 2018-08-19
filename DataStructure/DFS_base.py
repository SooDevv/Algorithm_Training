# 6
# A B C
# B A D E
# C A F
# D B
# E B F
# F C E

def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited


if __name__ == '__main__':
    n = int(input())
    graph = {}

    for i in range(n):
        start, *others = input().split()
        graph[start] = set(others)

    s = input('시작할 node 입력 : ')
    result = dfs(graph, s)

    print(result)
