from __future__ import annotations


def radix_sort(arr: list[int]) -> list[int]:
    """Поразрядная сортировка, принимает список из ЦЕЛЫХ чисел.
    Время выполнения O(d(n+k)), память O(n+k)"""

    if not arr:
        return arr

    max_num: int = max(arr)
    exponent: int = 1

    while max_num // exponent > 0:
        buckets: list = [[] for _ in range(10)]

        for num in arr:
            digit = (num // exponent) % 10
            buckets[digit].append(num)

        arr = []
        for bucket in buckets:
            arr.extend(bucket)

        exponent *= 10

    return arr
