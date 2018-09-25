if __name__ == '__main__':
    n = int(input())
    numBook = {}

    for i in range(n):
        name, num = input().rstrip().split()
        numBook[name] = num

    for i in range(n):
        query = input()
        if query in numBook:
            print(query+'='+numBook[query])
        else:
            print('Not found')





