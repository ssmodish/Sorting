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
    sorting = True
    while sorting:
        sort_count = 0
        for i in range(0, len(arr)-1):
            if arr[i + 1] < arr[i]:
                swap = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = swap
                sort_count +=1
        if sort_count == 0:
            sorting = False

    return arr



# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
arr2 = []
arr3 = [1, 5, -2, 4, 3]

print(count_sort(arr1))
print(count_sort(arr2))
print(count_sort(arr3))