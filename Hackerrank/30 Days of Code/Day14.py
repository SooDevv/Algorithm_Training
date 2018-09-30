class Difference:
    def __init__(self, a):
        # a : list
        self.arr = a
        self.min = min(a)
        self.max = max(a)
        self.maximumDifference = None

    def computeDifference(self):
        self.maximumDifference = abs(self.min - self.max)
        return self.maximumDifference


if __name__ == '__main__':
    n = input()
    a = [int(e) for e in input().split(' ')]
    print(a)

    d = Difference(a)
    d.computeDifference()


    print(d.maximumDifference)