def binary_search(arr, target):
    low = 0
    high = len(arr) -1

    while low <=high:
        mid = int((low + high)/2)
        guess = arr[mid]

        if guess == target:
            return mid
        elif target < guess:
            high = mid-1
        else:
            low = mid +1
    return None


if __name__ == '__main__':
    arr = [1,3,5,7,9]
    res = binary_search(arr, 7)
    print(res)