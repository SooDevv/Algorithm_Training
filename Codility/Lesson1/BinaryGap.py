# Binary gap
# 10진수를 2진수로 바꾸고, 변환된 2진수 중에서 1과 1사이의 0의 갯수중 가장 큰 것 return


def solution(binary):
    i = 0
    max_cnt = 0
    cnt = 0
    flag = False

    for i in range(len(binary)):
        if binary[i] == '1':
            if flag:
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt = 0
            else:
                cnt = 0
                flag = True
        else:
            cnt += 1

    return max_cnt


if __name__ == '__main__':
    n = int(input())
    binary = bin(n)[2:]
    result = solution(binary)
    print(result)