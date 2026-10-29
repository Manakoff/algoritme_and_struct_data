from __future__ import annotations


def is_valid_brackets(text: str) -> bool:
    """Булевая функция для проверки коректности ввода скобок.
    Используется тип данных стек(LIFO).Время O(n), Память O(n).
    """

    stack: list[str] = []
    brackets_dict: dict = {"}": "{", "]": "[", ")": "("}

    for sym in text:
        if sym in brackets_dict.values():
            stack.append(sym)
        elif sym in brackets_dict:
            if not stack or stack.pop() != brackets_dict[sym]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    try:
        user_input: str = input("Введите строку: ")
        print("Строка валидна" if is_valid_brackets(user_input) else "Строка невалидна")

    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
