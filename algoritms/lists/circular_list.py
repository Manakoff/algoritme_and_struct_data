from __future__ import annotations


class Node:
    """Класс узел, преднозначен для записи объекта в список"""

    def __init__(self, data) -> None:
        self.data = data
        self.next: Node | None = None

    def __str__(self):
        return str(self.data)


class CircularLinkedList:
    def __init__(self) -> None:
        self.length: int = 0
        self.head: Node | None = None
        self.tail: Node | None = None

    def add_end(self, new_data):
        """Добавляет элемент в конец циклического списка.
        Сложность O(1)
        """
        new_node = Node(new_data)
        self.length += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            return

        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head

    def delete(self, value):
        """Удаляет элемент в циклическом спискe. Сложность O(n)"""
        if self.head is None:
            return "The list is empty"

        if self.head.data == value and self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return None

        if self.head.data == value:
            self.head = self.head.next
            self.tail.next = self.head
            self.length -= 1
            return None

        temp = self.head
        while temp.next != self.head:
            if temp.next.data == value:
                if temp.next == self.tail:
                    self.tail = temp

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

            while current.next != self.head:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    swap = True
                current = current.next

    def __len__(self) -> int:
        """Вывод длины списка"""
        return self.length

    def print_list(self) -> None:
        """Вывод циклического списка"""
        if self.head is None:
            print("List is empty\n")
            return

        temp = self.head
        while True:
            print(f"{temp.data}")
            temp = temp.next
            if temp == self.head:
                break
        print()


if __name__ == "__main__":

    llist = CircularLinkedList()

    llist.add_end(4)
    llist.add_end(3)
    llist.add_end(1)
    llist.add_end(2)
    llist.delete(1)
    llist.sort()

    llist.print_list()
    print(len(llist))
