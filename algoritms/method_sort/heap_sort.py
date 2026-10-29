from __future__ import annotations
from typing import List, Union

Num = Union[int, float]


def heapify(arr: List[Num], heap_size: int, root_index: int) -> None:
    """Функция 'просеивания' элемента вниз для поддержания свойств кучи"""

    largest: int = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]

        heapify(arr, heap_size, largest)


def heap_sort(arr: List[Num]) -> None:
    """Пирамидальная сортировка, время O(n*log(n)),
    память O(1)"""

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
