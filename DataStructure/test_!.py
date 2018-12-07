# 발판의 숫자들이 담긴 배열 steps가 주어졌을 때 토끼가 뛰어야 할 횟수를 반환하는 함수 crossBridge()의 빈칸을 채워 함수를 완성해봅시다.
# 예를들어 이렇게 호출하면
#
# crossBridge([1,1,3,5,2,3,5])
# Copy
# [1, 3, 3, 4 ]
# 다음 값이 반환됩니다.
# [1, 1, ]
#
# 4
# Copy
# ** 부연 설명 ** 1번째 칸이 숫자 1이므로 1칸 점프합니다.
# 2번째 칸이 숫자 1이므로 1칸 점프합니다.
# 3번째 칸이 숫자 2이므로 2칸 점프합니다.
# 5번째 칸이 숫자 5이므로 5칸 점프합니다. (도착)
# 4번 점프했으므로 4를 반환합니다.
#
#
# ****************************************

def crossBridge(steps):
    cnt = 0
    current = 0
    n = len(steps)
    while current < n:
        current += steps[current]
        cnt +=1
    return cnt

if __name__ == '__main__':
    res = crossBridge([1,100,1008,9000,10000,500000,7000000])
    print(res)