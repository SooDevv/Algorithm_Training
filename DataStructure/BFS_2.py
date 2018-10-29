# hello coding - bfs

from collections import deque


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anju', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anju'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True # 탐색 종료
            else:
                search_queue += graph[person]
                searched.append(person)

    return False

def person_is_seller(name):
    return name[-1] == 's'


if __name__ == '__main__':
    search('you')