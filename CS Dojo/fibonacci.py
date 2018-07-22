# fibonacci : 1, 1, 2, 3, 5, 8, 13, 21
import time

start_time = time.time()
print(start_time)

n = int(input())
memo = [0 for x in range(n +1)]

def fibonacci(n):
    if n == 0 or n ==1:
        return 1
    elif memo[n] > 0:
        return memo[n]
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]




if __name__ == '__main__':
   result = fibonacci(n)
   print(result)

   endtime = time.time()
   print('걸린시간',endtime - start_time)