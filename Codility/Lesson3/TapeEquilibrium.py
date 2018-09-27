# arr = [3, 1, 2, 4, 3], n = 5

def solution(arr):
    n = len(arr)
    minDif = abs(sum(arr[1:]) - sum(arr[:1])) # slice 후, sum()에서 시간복잡도 N*N

    for p in range(1, n):
        if sum(arr[p:]) == sum(arr[:p]):
            minDif = 0
            break

        dif = abs(sum(arr[p:]) - sum(arr[:p]))
        if dif < minDif:
            minDif = dif

    return minDif

# another solution
# slice 사용하지 않음, 배열에서 빼는 식으로 구현
def solution(arr):
    sum_left = 0
    sum_right = sum(arr)
    min_difference = None

    for i in range(1, len(arr)):
        sum_left += arr[i-1]
        sum_right -= arr[i-1]
        difference = abs(sum_left-sum_right)

        if min_difference == None:
            min_difference = difference
        else:
            min_difference = min(min_difference, difference)

    return min_difference

if __name__ == '__main__':
    res = solution([3, 1, 2, 4, 3])
    print(res)