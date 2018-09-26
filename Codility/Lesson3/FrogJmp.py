#x=10, y=85, d=30
# return 3
import math

def solution(X, Y, D):
    return int(math.ceil((Y-X) / D))

if __name__ == '__main__':
    res = solution(10, 85, 30)
    print(res)