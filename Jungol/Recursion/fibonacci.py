def fibo(n):
    if n ==0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


result = fibo(5)
print(result)

# 0, 1, 2, 3, 4, 5, 6, 7,  8,  9
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55