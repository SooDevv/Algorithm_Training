def matchingStrings(strings, queries):
    result = []
    for query in queries:
        count = strings.count(query)
        result.append(count)
    return result

n = int(input())
strings = []

for i  in range(n):
    string = input()
    strings.append(string)

m = int(input())
queries = []

for i in range(m):
    query = input()
    queries.append(query)

res = matchingStrings(strings, queries)

##한 줄 씩 print 하는 법
# for i in res:
#     print(i)
print('\n'.join(map(str, res)))


1469645342