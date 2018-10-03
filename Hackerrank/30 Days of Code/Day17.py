class Calculator:
    def power(self, i, j):
        if i < 0 or j < 0:
            return 'n and p should be non-negative'
        return i ** j

if __name__ == '__main__':
    myCalculator = Calculator()
    T = int(input())
    for _ in range(T):
        i, j = map(int, input().rstrip().split())

        try:
            ans = myCalculator.power(i,j)
            print(ans)
        except Exception as e:
            print(e)