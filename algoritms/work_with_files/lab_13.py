import re
import os
from typing import List, Optional, Set


def get_hash(word: str, table_size: int) -> int:
    """Полиномальная хеш-функция"""
    hash_value: int = 0
    p: int = 31
    m: int = 10**9 + 7
    for symbol in word:
        hash_value = (hash_value * p + ord(symbol)) % m

    return hash_value % table_size


def read_words_from_file(file_path: str) -> List[str]:
    """Считывает файл и убирает шум"""
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", encoding="utf-8") as f:
        text: str = f.read().lower()

    words: List[str] = re.findall(r"[a-zа-яё\-]+", text)
    unique_words: Set[str] = set(words)
    return list(unique_words)


class HashTableOpenAddressing:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.table: List[Optional[str]] = [None] * size

    def insert(self, word: str) -> bool:
        """Вставка методом линейного наложения"""

        init_hash: int = get_hash(word, self.size)

        for i in range(self.size):
            c_index: int = (init_hash + i) % self.size
            if self.table[c_index] is None:
                self.table[c_index] = word
                return True
            if self.table[c_index] == word:
                return True
        return False

    def save_to_file(self, file_path: str) -> None:
        """Сохранение в формате таблицы"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"{'Индекс':<8} | {'Значение':<20}\n")
            for idx, item in enumerate(self.table):
                val: str = item if item is not None else "<пусто>"
                f.write(f"{idx:<8} | {val:<20}\n")


if __name__ == "__main__":
    input_filename: str = "input.txt"
    output_filename: str = "result_lab13.txt"

    words_list: List[str] = read_words_from_file(input_filename)
    table_size: int = int(len(words_list) * 1.5) if words_list else 10
    if table_size < 10:
        table_size = 10

    table: HashTableOpenAddressing = HashTableOpenAddressing(table_size)

    for word in words_list:
        table.insert(word)

    table.save_to_file(output_filename)
