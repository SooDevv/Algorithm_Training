# Interface
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        # n의 약수를 구해서 다 더하라
        # 12 = 1, 2, 3, 4, 6, 12 = 28
        arr = []
        for i in range(1, n+1):
          if n % i == 0:
            arr.append(i)
        return sum(arr)


if __name__ == '__main__':
    n = int(input())
    my_calculator = Calculator()
    s = my_calculator.divisorSum(n)
    print("I implemented: " + type(my_calculator).__bases__[0].__name__)
    print(s)