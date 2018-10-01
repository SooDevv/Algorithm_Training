def solution(arr):
    m = max(arr)
    n = len(arr)

    if m != n or n != len(set(arr)):
        return 0
    else:
        return 1