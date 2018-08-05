# DFS : 탐색을 시작한 노드로부터 너무 멀어지게 되어 즉시 그만두고 싶을 떄 사용하면 효과적
#       트리 순회 기법은 전부 DFS
#       과거 위치의 인접 노드보다 현재 위치의 인접 노드를 먼저 방문하기 때문에 stack 사용

# undirected graph
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

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
    start = input('시작할 node 입력:')

    result = dfs(graph, start)

    print(result)