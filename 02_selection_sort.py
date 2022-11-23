"""
Selection sort in Python
Sorting by finding min_index

Time complexity: O(n2).
Space complexity of O(1).
"""

import random
import time


def selection_sort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])

    return array


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
print('Unordered List:', arr)
selection_sort(arr, size)
print('Ordered List:', arr)
print('-' * 100)

input_number = int(input('Select the amount of random numbers to order: '))
input_list = [random.randint(1, 100) for x in range(input_number)]
print('Unordered List:', input_list)
start = time.time()
new_list = selection_sort(input_list, len(input_list))
end = time.time()
print('Ordered List Descending:', new_list)
print('Miliseconds Time:', round((end - start) * 1000))
