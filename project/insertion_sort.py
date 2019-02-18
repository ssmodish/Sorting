def insertion_sort(arr):
    for i in range(1, len(arr)):
        swap = arr[i]
        j = i - 1
        while j >= 0 and swap < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = swap

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = [12, 11, 13, 5, 6]
arr3 = [0, 1, 2, 3, 4, 5]

print(insertion_sort(arr2))
