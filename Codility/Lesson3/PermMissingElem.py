def solution(arr):
    li = [0] * (len(arr) + 1)
    for i in arr:
        li[i-1] = 1
    return li.index(0) + 1


# another solution
# this is very fancy.......
def solution(arr):
    return sum(range(len(arr)+2)) - sum(arr)





if __name__ == '__main__':
    result = solution([2,3,1,5])
    print(result)