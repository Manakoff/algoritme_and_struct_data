from __future__ import annotations
from typing import List, Union

Num = Union[int, float]


def merge(left_list: List[Num], right_list: List[Num]) -> List[Num]:
    """Принимает два отсортированных (более простых списка),
    сливает их в один более сложный список и возвращает его
    """

    sorted_list: List[Num] = []
    left_list_index: int = 0
    right_list_index: int = 0
    left_list_len: int = len(left_list)
    right_list_len: int = len(right_list)

    for _ in range(left_list_len + right_list_len):
        if left_list_index < left_list_len and right_list_index < right_list_len:

            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_len:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_len:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(arr: List[Num]) -> List[Num]:
    """Сортировка слиянием, время выполнения O(n*log(n)), память O(n)"""

    if len(arr) <= 1:
        return arr

    mid: int = len(arr) // 2
    left_list: List[Num] = merge_sort(arr[:mid])
    right_list: List[Num] = merge_sort(arr[mid:])

    return merge(left_list, right_list)
