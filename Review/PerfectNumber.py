n = int(input())

def isPerfect(num):
    total = 0
    for i in range(1, num+1):
        if num % i == 0:
            total += i
    print(total)
    b = 'True' if num == total/2 else 'False'
    return b

print(isPerfect(n))

