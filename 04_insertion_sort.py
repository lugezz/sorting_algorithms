"""
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing
cards in your hands. The array is virtually split into a sorted and an unsorted part.
Values from the unsorted part are picked and placed at the correct position in the sorted part.

Time complexity: O(n2).
Space complexity of O(1).
"""

import random
import time


def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def insertion_sort_2(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1

    return arr


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
print('Unordered List:', arr)
insertion_sort(arr)
print('Ordered List:', arr)
print('-' * 100)

input_number = int(input('Select the amount of random numbers to order: '))
input_list = [random.randint(1, 100) for x in range(input_number)]
print('Unordered List:', input_list)
start = time.time()
new_list = insertion_sort(input_list)
end = time.time()
print('Ordered List:', new_list)
print('Miliseconds Time:', round((end - start) * 1000))
