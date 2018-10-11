from collections import Counter


def makeAnagram(a, b):
    s1 = dict(Counter(a)-Counter(b))
    s2 = dict(Counter(b)-Counter(a))

    cnt = sum(s1.values()) + sum(s2.values())
    return cnt


if __name__ == '__main__':
    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)