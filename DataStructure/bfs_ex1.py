from collections import deque

graph = {}
graph['s'] = ['a', 'b', 'c']
graph['a'] = ['s', 'f']
graph['b'] = []
graph['c'] = ['s', 'd']
graph['d'] = ['c', 'f']
graph['f'] = ['a', 'd']

def search(start):
    search_queue = deque()
    search_queue += graph['s']
    visited = ['s']

    while search_queue:
        location = search_queue.popleft()
        if not location in visited:
            if location == 'f':
                return visited
            else:
                search_queue += graph[location]
                visited.append(location)
        return visited

    return False



if __name__ == '__main__':
    res = search('s')
    print(res)