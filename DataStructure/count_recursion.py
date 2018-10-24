def count_recursion(arr):
    if len(arr) < 1:
        return 0

    else:
        return 1+ count_recursion(arr[1:])



if __name__ == '__main__':
    res = count_recursion([1,2,3,4,5,6,7,8,9])
    print(res)