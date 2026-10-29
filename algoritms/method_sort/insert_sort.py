from __future__ import annotations
from typing import List, Union


def insert_sort(arr: List[Union[int, float]]) -> None:
    """Сортировка списка вставками, время выполнения O(n^2), память O(1)"""

    for i in range(1, len(arr)):
        item_to_insert: Union[int, float] = arr[i]
        j: int = i - 1

        while j >= 0 and arr[j] > item_to_insert:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = item_to_insert
