if __name__ == '__main__':
    t = int(input())

    for _ in range(t): # test case 수
        n = int(input()) # person 수

        q = list(map(int, input().rstrip().split()))

        bribes = 0
        valid = True

        for i in reversed(range(n)):
            v = i + 1

            if q[-1] == v:
                q.pop(-1)
            elif len(q) > 1 and q[-2] == v:
                q.pop(-2)
                bribes += 1
            elif len(q) > 2 and q[-3] == v:
                q.pop(-3)
                bribes += 2
            else:
                valid = False
                break

        if valid:
            print(bribes)
        else:
            print("Too chaotic")