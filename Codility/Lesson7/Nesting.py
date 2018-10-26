def solution(s):
    if len(s) == 0:
        return 1

    stack = []
    pair = {')':'('}

    for i in s:
        if i == '(':
            stack.append(i)
        elif len(stack) == 0:
            return 0
        elif pair[i] != stack.pop():
            return 0

    return 1 if len(stack) ==0 else 0

if __name__ == '__main__':
    res = solution('())')
    print(res)