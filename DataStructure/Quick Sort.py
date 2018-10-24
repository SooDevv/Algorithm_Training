def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i> pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    res = quicksort([10,5,2,3])
    print(res)