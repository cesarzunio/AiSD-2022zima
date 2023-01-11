from typing import Any, List


def bubble_sort(array: List[Any]):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j] >= array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


def selection_sort(array: List[Any], ascending: bool) -> None:
    for i in range(len(array) - 1):

        smallest_value = float('inf') if ascending else -float('inf')
        index_of_smallest_value = -1

        for j in range(i, len(array)):
            if (array[j] < smallest_value and ascending) or (array[j] >= smallest_value and not ascending):
                smallest_value = array[j]
                index_of_smallest_value = j

        temp = array[i]
        array[i] = array[index_of_smallest_value]
        array[index_of_smallest_value] = temp


def insertion_sort(tab3: List[Any]) -> None:
    length_of_array = len(tab3)
    index_of_value_higher_than_key = 0
    for k in range(1, length_of_array):
        key = tab3[k]
        for i in range(0, k):
            if tab3[i] > key:
                index_of_value_higher_than_key = i
                break
            else:
                index_of_value_higher_than_key = k

        if index_of_value_higher_than_key == k:
            # print('continue (m=k)')
            continue
        else:
            for i in range(k, index_of_value_higher_than_key, -1):
                tab3[i] = tab3[i - 1]
            tab3[index_of_value_higher_than_key] = key


arr = [2, 3, 1, 6, 3, 6, 2, 1, 0]
print(arr)
insertion_sort(arr)
print(arr)