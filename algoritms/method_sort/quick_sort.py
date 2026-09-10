from __future__ import annotations
from typing import List, Union

Num = Union[int, float]


def partition(arr: List[Num], low: int, high: int) -> int:
    """Схема разбиения Хоара.

    Выбирает опорный элемент и перегруппировывает массив:
    элементы меньше опорного уходят влево, больше — вправо.
    Возвращает индекс разделения
    """

    pivot: Num = arr[(low + high) // 2]
    i: int = low - 1
    j: int = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr: List[Num]) -> None:
    """Быстрая сортировка, время выполнения O(n*log(n)), память O(log(n))"""

    def _quick_sort(items: List[Num], low: int, high: int) -> None:
        if low < high:
            split_index: int = partition(items, low, high)

            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)
