def solution(s):
    N = len(s)
    if N == 0:
        return 1

    pair = {']':'[', '}':'{', ')':'('}
    to_push = ['[', '{', '(']
    stack = []

    for element in s:
        if element in to_push:
            stack.append(element)
        else:
            if len(stack) == 0:
                return 0
            elif pair[element] != stack.pop():
                return 0

    return 1 if len(stack)==0 else 0

if __name__ == '__main__':
    res = solution("{[)}")
    print(res)