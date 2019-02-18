# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp
    return arr



# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    for i in range(1, len(arr)):
        swap = arr[i]
        j = i - 1
        while j >= 0 and swap < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = swap

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    return arr
