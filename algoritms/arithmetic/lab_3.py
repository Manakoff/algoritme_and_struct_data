from __future__ import annotations
import math


def get_all_prime_factor(x: int) -> list:
    """Добавить описание"""
    res_list: list[int] = []

    for K in range(0, math.floor(math.log(x, 3) + 1e-9) + 1):
        for L in range(0, math.floor(math.log(x, 5) + 1e-9) + 1):
            for M in range(0, math.floor(math.log(x, 7) + 1e-9) + 1):
                res = 3**K * 5**L * 7**M
                if res <= x:
                    res_list.append(res)

    res_list.sort()
    return res_list


user_x: int = int(input())


if __name__ == "__main__":
    print(*get_all_prime_factor(user_x))
