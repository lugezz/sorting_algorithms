"""
Heapsort is a comparison-based sorting technique based on a Binary Heap data structure. It is
similar to selection sort where we first find the maximum element and place the maximum element
at the end. We repeat the same process for the remaining element.

Time complexity: O(n log n).
Space complexity of O(n).
"""

import random
import time


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    lft = 2 * i + 1  # left = 2*i + 1
    rth = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if lft < n and arr[i] < arr[lft]:
        largest = lft

    # See if right child of root exists and is
    # greater than root
    if rth < n and arr[largest] < arr[rth]:
        largest = rth

    # Change root, if needed
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap

    # Heapify the root.
        heapify(arr, n, largest)
    # The main function to sort an array of given size


def heap_sort(arr):
    n = len(arr)
    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)

    return arr


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
print('Unordered List:', arr)
new_arr = heap_sort(arr)
print('Ordered List:', new_arr)
print('-' * 100)

input_number = int(input('Select the amount of random numbers to order: '))
input_list = [random.randint(1, 100) for x in range(input_number)]
print('Unordered List:', input_list)
start = time.time()
new_list = heap_sort(input_list)
end = time.time()
print('Ordered List:', new_list)
print('Miliseconds Time:', round((end - start) * 1000))
