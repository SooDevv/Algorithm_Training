def solution(arr):
    max_num = max(arr)

    arr.sort()

    #case1 : +, +, +
    plus = arr[-2] * arr[-3] * max_num

    #case2: -, -, +
    minus = arr[0] * arr[1] * max_num

    return max(plus, minus)




if __name__ == '__main__':

    res = solution([-3,1,2,-2,5,6])
    print(res)