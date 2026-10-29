from __future__ import annotations


class DNode:
    """Класс узел, преднозначен для записи объекта в список"""

    def __init__(self, data) -> None:
        self.data = data
        self.prev: DNode | None = None
        self.next: DNode | None = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self) -> None:
        self.length: int = 0
        self.head: DNode | None = None
        self.tail: DNode | None = None

    def add_end(self, new_data) -> None:
        """Добавляет элемент в конец двусвязанного списка.
        Сложность O(1)
        """
        new_node = DNode(new_data)
        self.length += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def __len__(self) -> int:
        """Вывод длины списка"""
        return self.length

    def delete(self, value):
        """Удаляет первый найденный элемент в двусвязном списке по значению. Сложность O(n)"""
        current = self.head

        while current is not None:
            if current.data == value:
                if current.prev is None and current.next is None:
                    self.head = None
                    self.tail = None

                elif current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None

                elif current.next is None:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.length -= 1
                return True

            current = current.next

        return False

    def sort(self):
        """Сортировка пузырьком. Сложность O(n^2)"""
        if self.length <= 1:
            return

        for i in range(self.length):
            current = self.head
            swapped = False

            while current and current.next:
                if current.data > current.next.data:

                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

            if not swapped:
                break

    def print_list(self):
        """Вывод списка"""
        temp = self.head

        while temp:
            print(f"{temp.data}")
            temp = temp.next
        print()


if __name__ == "__main__":

    llist = DoublyLinkedList()

    llist.add_end(4)
    llist.add_end(3)
    llist.add_end(1)
    llist.add_end(2)
    llist.print_list()

    llist.delete(1)
    llist.print_list()

    llist.sort()

    llist.print_list()
    print(len(llist))
