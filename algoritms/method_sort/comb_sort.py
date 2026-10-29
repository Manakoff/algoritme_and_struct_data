from __future__ import annotations
from typing import List, Union

Num = Union[int, float]


def comb_sort(arr: List[Num]) -> List[Num]:
    """Сортировка методом прочесывания,
    Среднее время выполнения O(n*log(n)), худший O(n^2),
    память O(1)
    """

    n: int = len(arr)
    gap = n
    shrink = 1.3
    flag = True

    while gap > 1 or flag:

        gap = int(gap / shrink)
        if gap < 1:
            gap = 1

        flag = False
        for i in range(0, n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                flag = True

    return arr
