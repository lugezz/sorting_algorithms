"""
Order a list in ascending order
"""

import random

list_1 = [2, 3, 1, 5]
big_list = [random.randint(1, 3000) for x in range(1000)]


def simple_sorting(list_to_order: list) -> list:
    for i in range(len(list_to_order) - 1):
        for j in range(i+1, len(list_to_order)):
            if list_to_order[j] < list_to_order[i]:
                temp = list_to_order[j]
                list_to_order[j] = list_to_order[i]
                list_to_order[i] = temp

    return list_to_order


def simple_sorting_opt(list_to_order: list, ascending: bool = True) -> list:
    for i in range(len(list_to_order) - 1):
        for j in range(i+1, len(list_to_order)):
            if (list_to_order[j] < list_to_order[i] and ascending) or (list_to_order[j] > list_to_order[i] and not ascending):
                temp = list_to_order[j]
                list_to_order[j] = list_to_order[i]
                list_to_order[i] = temp

    return list_to_order


new_list = simple_sorting(list_1)
print(new_list)
print('-' * 100)

print(big_list)
print('-' * 100)
new_list = simple_sorting(big_list)
print(new_list)

print('-' * 100)
print('-' * 100)

input_number = int(input('Select the amount of random numbers to order: '))
input_list = [random.randint(1, 100) for x in range(input_number)]
print('Unordered list:', input_list)
print('-' * 100)
new_list = simple_sorting_opt(input_list)
print('Ordered List:', new_list)
new_list = simple_sorting_opt(input_list, False)
print('Ordered List Descending:', new_list)
