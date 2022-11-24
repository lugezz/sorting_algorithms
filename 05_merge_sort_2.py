"""
Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself
for the two halves and then merges the two sorted halves. The merge() function is used for
merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and
arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
Merge sort = recursively divide array in 2, sort, re-combine

Time complexity: O(n log n).
Space complexity of O(n).
"""

import random
import time


# Function to merge ordered lists
def merge(sorted_left_list: list, sorted_right_list: list) -> list:
    resp = []

    while len(sorted_left_list) > 0 and len(sorted_right_list) > 0:
        if sorted_left_list[0] < sorted_right_list[0]:
            resp.append(sorted_left_list[0])
            sorted_left_list.pop(0)
        else:
            resp.append(sorted_right_list[0])
            sorted_right_list.pop(0)

    while len(sorted_left_list) > 0:
        resp.append(sorted_left_list[0])
        sorted_left_list.pop(0)

    while len(sorted_right_list) > 0:
        resp.append(sorted_right_list[0])
        sorted_right_list.pop(0)

    return resp


# Function to divide the lists in the two sublists
def merge_sort(list_to_order: list):
    if len(list_to_order) == 1:
        return list_to_order

    middle = len(list_to_order) // 2
    left_list = list_to_order[:middle]
    right_list = list_to_order[middle:]

    sorted_left_list = merge_sort(left_list)
    sorted_right_list = merge_sort(right_list)

    return merge(sorted_left_list, sorted_right_list)


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
print('Unordered List:', arr)
merge_sort(arr)
print('Ordered List:', arr)
print('-' * 100)

input_number = int(input('Select the amount of random numbers to order: '))
input_list = [random.randint(1, 100) for x in range(input_number)]
print('Unordered List:', input_list)
start = time.time()
new_list = merge_sort(input_list)
end = time.time()
print('Ordered List:', new_list)
print('Miliseconds Time:', round((end - start) * 1000))
