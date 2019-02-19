# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort(arr, low, high):
    # End condition: marker is lower than low
    if low >= high:
        return

    # define the divider between numbers lower than the pivot and numbers higher
    marker = low

    # rearrange numbers in array so that all numbers to the left of pivot are smaller
    # and all numbers to the right are greater
    for i in range(low, high):
        if arr[i] < arr[high]:
            swap = arr[i]
            arr[i] = arr[marker]
            arr[marker] = swap

            marker += 1

    swap = arr[high]
    arr[high] = arr[marker]
    arr[marker] = swap

    # do the same for all of the other numbers in the array
    quick_sort(arr, low, marker - 1)
    quick_sort(arr, marker + 1, high)
    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(quick_sort(arr1, 0, len(arr1)-1))
