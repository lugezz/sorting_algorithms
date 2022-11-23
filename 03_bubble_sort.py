"""
The bubble sort algorithm is a reliable sorting algorithm. This algorithm has a worst-case time
complexity of O(n2). The bubble sort has a space complexity of O(1). The number of swaps in
bubble sort equals the number of inversion pairs in the given array. When the array elements are
few and the array is nearly sorted, bubble sort is effective and efficien
"""

import random
import time


def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        flag = 0
        for j in range(0, arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = 1
                if flag == 0:
                    break
    return arr


def bubble_sort_2(list_to_order: list) -> list:
    for i in range(len(list_to_order)-1, 0, -1):
        for j in range(i):
            if list_to_order[j] > list_to_order[j+1]:
                list_to_order[j+1], list_to_order[j] = list_to_order[j], list_to_order[j+1]

    return list_to_order


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
print('Unordered List:', arr)
bubble_sort_2(arr)
print('Ordered List:', arr)
print('-' * 100)

# Output: List sorted with bubble sort in ascending order:  [1, 2, 3, 4, 5]

input_number = int(input('Select the amount of random numbers to order: '))
input_list = [random.randint(1, 100) for x in range(input_number)]
print('Unordered List:', input_list)
start = time.time()
new_list = bubble_sort_2(input_list)
end = time.time()
print('Ordered List Descending:', new_list)
print('Miliseconds Time:', round((end - start) * 1000))
