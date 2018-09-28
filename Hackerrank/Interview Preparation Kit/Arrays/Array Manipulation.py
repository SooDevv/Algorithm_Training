# 5 3 --> list = 5, test = 3
# 1 2 100 --> 1~2 까지 +100
# 3 5 200 --> 3~5 까지 +200
# 2 4 100 --> 2~4 까지 +100
def arrayManipulation(n, queries):
    # Big O (N)
    res = [0] * (n + 1)  # we only really need one terminal row, since we're applying each pass to all rows below

    # loop through all the queries and apply the increments/decrements for each
    # Big O (M) (size of queires)
    for row in range(len(queries)):
        a = queries[row][0]
        b = queries[row][1]
        k = queries[row][2]

        res[a - 1] += k  # increment the starting position
        # this is where a loop would increment everything else between a & b by k
        # but instead of taking b-a steps, we take a constant 2 steps, saving huge on time
        res[b] -= k  # decrement the position AFTER the ending position

    # now loop through res one time - Big O (N) (size of res)
    sm = 0  # running sum
    mx = 0  # maximum value found so far
    for i in range(len(res)):
        sm += res[i]
        if sm > mx:
            mx = sm

    # total run time is Big O (2*N + M) >> Big O(N)
    return mx

def arrayManipulation(n, queries):

    arr = [0] * (n+1)


    while queries:
        query = queries.pop(0)
        arr[query[0]:query[1]+1] += query[2]


    # for s, e, num in queries:
    #     for i in range(s,e+1):
    #         arr[i] += num

    return max(arr)



if __name__ == '__main__':
    nm = input().rstrip().split()

    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)