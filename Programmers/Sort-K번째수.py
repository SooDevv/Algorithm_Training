def solution(array, commands):
    answer = []

    for i in commands:
        start = i[0]-1
        end = i[1]-1
        query = i[2]-1

        sub_arr= array[start:end+1]
        sub_arr.sort()
        answer.append(sub_arr[query])

    return answer


# 다른 풀이
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        # print(i, j, k)
        answer.append(list(sorted(array[i-1:j]))[k-1])

    return answer

if __name__ == '__main__':
    res = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    print(res)