import re
import os
from typing import List, Set


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


class HashTableChaining:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.table: List[List[str]] = [[] for _ in range(size)]

    def insert(self, word: str) -> None:
        """Вставка методом цепочек"""

        index: int = get_hash(word, self.size)
        if word not in self.table[index]:
            self.table[index].append(word)

    def save_to_file(self, file_path: str) -> None:
        """Сохранение в формате таблицы"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"{'Индекс':<8} | {'Связанный список':<50}\n")
            for idx, item in enumerate(self.table):
                val: str = " -> ".join(item) if item else "<пусто>"
                f.write(f"{idx:<8} | {val:<50}\n")


if __name__ == "__main__":
    input_filename: str = "input.txt"
    output_filename: str = "result_lab14.txt"

    words_list: List[str] = read_words_from_file(input_filename)
    table_size: int = int(len(words_list) * 1.5) if words_list else 10
    if table_size < 10:
        table_size = 10

    table: HashTableChaining = HashTableChaining(table_size)

    for word in words_list:
        table.insert(word)

    table.save_to_file(output_filename)
