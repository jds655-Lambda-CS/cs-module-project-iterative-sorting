def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    working_arr = arr[:]
    float = 0
    while len(working_arr) != 0:
        mid = len(working_arr) // 2
        value = working_arr[mid]
        if target == value:
            if float
            return float - mid
        if target > value:
            working_arr = working_arr[mid:]
        elif target < value:
            working_arr = working_arr[0:mid]
            float += len(arr) - len(working_arr)
    return -1

#
# arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
# print(binary_search(arr1, 0) == 6)