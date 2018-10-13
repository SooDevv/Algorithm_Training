def solution(arr):
    result = 0
    meetzero = 0

    for i in arr:
        if i == 0:
            meetzero += 1
        else:
            result += meetzero

    if result > 1000000000 or result <0:
        return -1

    return result

print(solution([0,1,0,1,1]))