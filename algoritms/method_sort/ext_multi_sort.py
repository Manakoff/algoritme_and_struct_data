import heapq
import os
from contextlib import ExitStack
from typing import List, Generator


def read_in_chunks(file_path: str, chunk_size: int) -> Generator[List[int], None, None]:
    """Генератор, который считывает файл порциями фиксированного размера."""
    with open(file_path, "r", encoding="utf-8") as f:
        chunk: List[int] = []
        for line in f:
            chunk.append(int(line.strip()))
            if len(chunk) == chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk


def create_initial_runs(input_filename: str, run_size: int = 1024) -> List[str]:
    """Разбивает большой файл на маленькие отсортированные файлы-прогоны."""
    runs: List[str] = []

    for run_idx, chunk in enumerate(read_in_chunks(input_filename, run_size)):
        chunk.sort()
        run_filename: str = f"run_{run_idx}.tmp"

        with open(run_filename, "w", encoding="utf-8") as rf:
            for item in chunk:
                rf.write(f"{item}\n")

        runs.append(run_filename)

    return runs


def merge_runs(run_files: List[str], output_filename: str) -> None:
    """Выполняет многопутевое слияние (N-way merge) файлов-прогонов в один результирующий файл."""
    min_heap: List[tuple[int, int]] = []

    with ExitStack() as stack, open(output_filename, "w", encoding="utf-8") as out_f:
        files = [stack.enter_context(open(fname, "r", encoding="utf-8")) for fname in run_files]

        for file_idx, f in enumerate(files):
            line: str = f.readline()
            if line:
                val: int = int(line.strip())
                heapq.heappush(min_heap, (val, file_idx))

        while min_heap:
            val, file_idx = heapq.heappop(min_heap)
            out_f.write(f"{val}\n")

            next_line: str = files[file_idx].readline()
            if next_line:
                next_val: int = int(next_line.strip())
                heapq.heappush(min_heap, (next_val, file_idx))

    for fname in run_files:
        if os.path.exists(fname):
            os.remove(fname)


def external_polyphase_sort(
        input_filename: str,
        output_filename: str,
        run_size: int = 1024
) -> None:
    """Основная функция внешней многофазной сортировки."""
    print("1. Создание начальных прогонов...")
    runs: List[str] = create_initial_runs(input_filename, run_size=run_size)

    print(f"2. Слияние {len(runs)} прогонов...")
    merge_runs(runs, output_filename)
    print("Сортировка завершена!")
