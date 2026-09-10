from __future__ import annotations
from typing import List, Union


def selection_sort(arr: List[Union[int, float]]) -> None:
    """Сортировка списка выбором, время выполнения O(n^2), память O(1)"""

    for i in range(len_arr := len(arr)):
        smallest_index: int = i

        for j in range(i + 1, len_arr):
            if arr[j] < arr[smallest_index]:
                smallest_index: int = j

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
