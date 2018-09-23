def review(s):
    # h a c k e r
    odd = []
    even = []
    for i, c in enumerate(s):
        if i % 2 == 0: #짝수
            odd.append(s[i])
        else:
            even.append(s[i])
    return ''.join(odd) + ' '+ ''.join(even)


if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        s = input()
        result = review(s)
        print(result)

