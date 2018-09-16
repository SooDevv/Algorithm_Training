#한 번에 다하려고 하지말고
#쪼개서 (부분 문제로 나눠서 풀 것)

def repeatedString(s, n):
    a_cnt = 0
    for i in s:
        if i == 'a':
            a_cnt += 1

    res = a_cnt * (n//len(s)) # 몫

    for i in s[:n%len(s)]: # 나머지
        if i == 'a':
            res += 1

    return res

if __name__ == '__main__':
    s = input()
    n = int(input())

    result = repeatedString(s, n)
    print(result)
