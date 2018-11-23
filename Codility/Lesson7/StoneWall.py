#h0는 왼쪽 벽 끝의 높이
#hn-1은 오른쪽 벽 끝의 높이

H = [8, 8, 5, 7, 9, 8, 7, 4, 8]

# def solution(H):
#     cnt = 0
#     stack = [H[0]]
#
#     if len(H) == 0:
#         return 0
#     elif len(H) == 1:
#         return 1
#
#     for i in H[1:]:
#
#         cur = stack[-1]
#
#         while cur > i and len(stack)>0:
#             cur = stack.pop()
#             cnt += 1
#
#         stack.append(i)
#
#     return cnt


def solution(H):
    blocks, previous, stack = 0, 0, []
    for current in H:
        if current > previous:
            blocks +=1

        elif current < previous:
            existing = previous
            while len(stack) and stack[-1] >= current:
                existing = stack.pop()
            blocks += 1 if existing!= current else 0
        previous = current
        stack.append(previous)
    return blocks

if __name__ == '__main__':
    res = solution(H)
    print(res)




