# <<input>>
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# def dfs(graph, start):
#     visited = []
#     stack = [start]
#
#     while stack:
#         n = stack.pop()
#         if n not in visited:
#             visited.append(n)
#             stack += graph[n] - visited
#     return visited

def asd(node, visited):
    visited = []
    for a in graph[node]:
        if a not in visited:
            asd(a, visited.append(a))
    return visited

if __name__ == '__main__':
    node, edge, start = input().split()
    graph = {}

    for i in range(int(edge)):
        n1, n2 = input().split()

        if n1 in graph:
            graph[n1].append(n2)

        else:
            graph[n1] = [n2]

    # print(graph)

    # result = dfs(graph, start)
    # print(result)

    result = asd('1',0)
    print(result)
