# 문제: 두개의 문자열 중에서 공통 원소인게 하나라도 있는지 알아내는 문제
# set의 성질을 이용한다.
# 서로 다른 문자열의 공통 부분이 있다면 = 교집합이 true라는 것

def twoStrings(s1, s2):
    if set(s1) & set(s1):
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s1 = input()
        s2 = input()

        result = twoStrings(s1, s2)
        print(result)