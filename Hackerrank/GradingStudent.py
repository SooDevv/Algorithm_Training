# 73 의 다음 5의 배수 구하기
# 5의 배수 - 73 < 3
# 73 67 38 33

def finalScore(arr):
    mul_five = []
    for i in arr:
        i += 5 - (i % 5)
        mul_five.append(i)

    return mul_five



if __name__ == '__main__':
    n = int(input())

    grades = []
    for _ in range(n):
        score = int(input())
        grades.append(score)

    result = finalScore(grades)
    print(result)