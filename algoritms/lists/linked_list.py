from __future__ import annotations


class Node:
    """Класс узел, преднозначен для записи объекта в список"""

    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self) -> None:
        self.length: int = 0
        self.head: Node | None = None

    def add_home(self, new_data) -> None:
        """Добавляет элемент в начало односвязанного списка.
        Сложность O(1)
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def add_end(self, new_data):
        """Добавляет элемент в конец односвязанного списка.
        Сложность O(1)
        """
        new_node = Node(new_data)
        self.length += 1
        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

    def delete(self, value):
        """Удаляет элемент в односвязаном списке по значению. Сложность O(n)"""
        if self.head is None:
            return "The list is empty"

        if self.head.data == value:
            self.head = self.head.next
            return None
        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                self.length -= 1
                return None
            temp = temp.next

        return "Value not found in the list"

    def sort(self):
        """Сортировка пузырьком"""
        if self.head is None or self.head.next is None:
            return

        swap = True
        while swap:
            swap = False
            current = self.head

            while current.next is not None:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swap = True
                current = current.next

    def __len__(self) -> int:
        """Вывод длины списка"""
        return self.length

    def print_list(self):
        """Вывод списка"""
        temp = self.head

        while temp:
            print(f"{temp.data}")
            temp = temp.next
        print()


if __name__ == "__main__":

    llist = LinkedList()

    llist.add_end(4)
    llist.add_end(3)
    llist.add_end(1)
    llist.add_end(2)
    llist.delete(1)
    llist.sort()

    llist.print_list()
    print(len(llist))
