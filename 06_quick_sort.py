"""
Quicksort is a sorting algorithm based on the divide and conquer approach where:

1. An array is divided into subarrays by selecting a pivot element (element selected from the
array).
While dividing the array, the pivot element should be positioned in such a way that elements
less than pivot are kept on the left side and elements greater than pivot are on the right side
of the pivot.

2. The left and right subarrays are also divided using the same approach. This process continues
until each subarray contains a single element.

3. At this point, elements are already sorted. Finally, elements are combined to form a sorted
array.

Time complexity: O(n log n).
Space complexity of O(n).
"""

import random
import time


def quick_sort(list_to_order: list) -> list:
    if len(list_to_order) < 1:
        return list_to_order
    else:
        pivot = list_to_order.pop()

    items_greater = []
    items_lower = []

    for item in list_to_order:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
print('Unordered List:', arr)
new_arr = quick_sort(arr)
print('Ordered List:', new_arr)
print('-' * 100)

input_number = int(input('Select the amount of random numbers to order: '))
input_list = [random.randint(1, 100) for x in range(input_number)]
print('Unordered List:', input_list)
start = time.time()
new_list = quick_sort(input_list)
end = time.time()
print('Ordered List:', new_list)
print('Miliseconds Time:', round((end - start) * 1000))
