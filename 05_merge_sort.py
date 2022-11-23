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


# funtion to divide the lists in the two sublists
def merge_sort(list_to_order: list, left_index: int = 0, right_index: int = -1):
    right_index = len(list_to_order) if right_index == -1 else right_index
    if left_index >= right_index:
        return list_to_order

    middle = (left_index + right_index) // 2
    merge_sort(list_to_order, left_index, middle)
    merge_sort(list_to_order, middle + 1, right_index)
    merge(list_to_order, left_index, right_index, middle)

    return list_to_order


# Defining a function for merge the list
def merge(list1, left_index, right_index, middle):
    # Creating subparts of a lists
    left_sublist = list1[left_index:middle + 1]
    right_sublist = list1[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each list1
    left_sublist_index = 0
    right_sublist_index = 0
    sorted_index = left_index

    # traverse both copies until we get run out one element
    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):

        # If our left_sublist has the smaller element, put it in the sorted
        # part and then move forward in left_sublist (by increasing the pointer)
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
            list1[sorted_index] = left_sublist[left_sublist_index]
            left_sublist_index = left_sublist_index + 1
        # Otherwise add it into the right sublist
        else:
            list1[sorted_index] = right_sublist[right_sublist_index]
            right_sublist_index = right_sublist_index + 1

        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # we will go through the remaining elements and add them
    while left_sublist_index < len(left_sublist):
        list1[sorted_index] = left_sublist[left_sublist_index]
        left_sublist_index = left_sublist_index + 1
        sorted_index = sorted_index + 1

    while right_sublist_index < len(right_sublist):
        list1[sorted_index] = right_sublist[right_sublist_index]
        right_sublist_index = right_sublist_index + 1
        sorted_index = sorted_index + 1


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
