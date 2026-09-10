from __future__ import annotations
from typing import List, Union

Num = Union[int, float]


def shell_sort(arr: List[Num]) -> List[Num]:
    """Cортировкa Шелла"""

    n: int = len(arr)
    gap: int = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp: Num = arr[i]
            j: int = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        gap //= 2

    return arr
