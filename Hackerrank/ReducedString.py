# a a a b c c c c
# list 로 생각
def super_reduced_stiring(s):
    even = []
    for c in s:
        if even and c == even[-1]:
            even.pop()
        else:
            even.append(c)
    return ''.join(even)


if __name__ == '__main__':
    s = input().strip()

    result = super_reduced_stiring(s)

    print(result) if result != '' else print('Empty String')

