def quick_sort(arr, low, high):
    if low >= high:
        return

    marker = low

    for i in range(low, high):
        if arr[i] < arr[high]:
            arr[marker], arr[i] = arr[i], arr[marker]
            marker += 1

    arr[marker], arr[high] = arr[high], arr[marker]

    quick_sort(arr, low, marker - 1)
    quick_sort(arr, marker + 1, high)
    return arr
