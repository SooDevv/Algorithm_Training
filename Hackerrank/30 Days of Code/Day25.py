def IsPrimeNum(d):
    if d ==1:
        return False
    elif d ==2 :
        return True

    import math
    sq = int(math.sqrt(d))
    print(sq)
    for i in range(2, sq+1):
        if d % i == 0:
            return False
    return True


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        d = int(input())
        res = "Prime" if (IsPrimeNum(d)) else "Not prime"
        print(res)