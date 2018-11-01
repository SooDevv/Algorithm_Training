from collections import deque

graph = {}
graph['CAB'] = ['CAR', 'CAT']
graph['CAR'] = ['BAR', 'CAT']
graph['BAR'] = ['BAT']
graph['CAT'] = ['BAT', 'MAT']
graph['MAT'] = ['BAT']
graph['BAT'] = []

def search(start):
    search_queue = deque()
    search_queue += graph['CAB']
    visited = ['CAB']

    while search_queue:
        node = search_queue.popleft()
        if not node in visited:
            if node == 'BAT':
                visited.append(node)
                return visited
            else:
                search_queue += graph[node]
                visited.append(node)
        return visited
    # return False


if __name__ == '__main__':
    res = search('CAB')
    print(res)