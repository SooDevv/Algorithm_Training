# 최대 공약수
# step1: base case

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


result = gcd(8, 10)
print(result)