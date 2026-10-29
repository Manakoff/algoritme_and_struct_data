from __future__ import annotations
from typing import Union, List
from is_valid_brackets import is_valid_brackets
import operator

TOKEN = Union[float, str]
OPERATOR = {
    "+": (operator.add, 1),
    "-": (operator.sub, 1),
    "*": (operator.mul, 2),
    "/": (operator.truediv, 2),
}


class ValidBracketError(Exception):
    """Исключение, преднозначенное для отлавливания ошибок
    в области скобок."""

    pass


def to_token(expression: str) -> List[TOKEN]:
    """Вункция для перевода выражения в токены,
    для дальнейшего использования в алгоритме
    сортировочной станции."""

    tokens: List[TOKEN] = []
    number: str = ""

    for i in expression:
        if i.isnumeric():
            number += i

        elif i == ".":
            if "." in number:
                raise ValueError("Некорректный формат числа (слишком много точек)")
            number += i

        elif i in ["+", "-", "*", "/", "=", "(", ")"]:
            if number != "":
                tokens.append(float(number))
                number = ""
            tokens.append(i)

        elif i != " ":
            raise TypeError("Введен неизвестный символ")

    if number != "":
        tokens.append(float(number))

    return tokens


def shunting_yard(tokens_expression: List[TOKEN]) -> List[TOKEN]:
    """Реализация сортировочной станции"""

    output: List[TOKEN] = []
    stack: List[str] = []

    for token in tokens_expression:
        if isinstance(token, float):
            output.append(token)

        elif token == "(":
            stack.append(token)

        elif token in (")", "="):
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()

        elif token in OPERATOR:
            priority = OPERATOR[token][1]

            while (
                stack and stack[-1] in OPERATOR and OPERATOR[stack[-1]][1] >= priority
            ):
                output.append(stack.pop())

            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


def calculate(rpn_expression: List[TOKEN]) -> float:
    """Функция посчёта арифметического выражения
    возвращает float."""

    stack: List[float] = []

    for token in rpn_expression:
        if isinstance(token, float):
            stack.append(token)

        elif token in OPERATOR:
            y = stack.pop()
            x = stack.pop()
            try:
                func = OPERATOR[token][0]
                res = func(x, y)
            except ZeroDivisionError as e:
                raise ZeroDivisionError("Ошибка: Попытка деления на ноль") from e

            stack.append(res)

    return stack[0]


if __name__ == "__main__":

    try:
        expr: str = input("Введите выражение:\n")
        if not is_valid_brackets(expr):
            raise ValidBracketError("Строка невалидна(проверьте корректность скобок)")
        else:
            print(calculate(shunting_yard(to_token((expr)))))

    except ZeroDivisionError as e:
        print(e)

    except ValidBracketError as e:
        print(e)

    except TypeError as e:
        print(e)

    except ValueError as e:
        print(e)

    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
