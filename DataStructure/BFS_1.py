# BFS: 그래프 내 모든 노드를 방문하고 싶을때
#      찾는 것을 발견할 때까지 모든 노드를 적어도 한 번은 방문하고 싶을때 사용
#      시작 노드로부터 차례로 인접 노드들을 queue 에 추가하여 구현

# undirected graph
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited


if __name__ == '__main__':
    start = input('시작할 node 입력: ')
    result = bfs(graph, start)
    print(result)
    print("dd")