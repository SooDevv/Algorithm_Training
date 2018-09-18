# 8
# UDDDUDUU

def countingValleys(n, s):
    depth = 0
    cnt = 0
    for i in range(n): #index가 필요
        if s[i] == 'D':
            cnt -= 1
        else:
            cnt += 1
        if cnt == 0 and s[i] == 'U':
            depth += 1
    return depth


if __name__ == '__main__':
    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)