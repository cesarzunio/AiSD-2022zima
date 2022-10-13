from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any):
        self.value = value
        self.next = None

    def __str__(self):
        return f'Node Value: {self.value}'


class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        outputText = ''
        pointer = self.head
        while True:
            if pointer.next is None:
                outputText += f'{pointer.value}'
                return outputText
            outputText += f'{pointer.value} -> '
            pointer = pointer.next

    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        if self.tail is not None:
            self.tail.next = node
        self.tail = node

    def node(self, at: int):
        pointer = self.head
        counter = 0
        while True:
            if counter == at or pointer.next is None:
                return pointer
            counter += 1
            pointer = pointer.next

    def insert(self, value: Any, at: int) -> None:
        pointer = self.head
        counter = 0
        while True:
            if counter == at:
                node = Node(value)
                node.next = pointer.next
                pointer.next = node
                return None
            if pointer.next is None:
                return None
            counter += 1
            pointer = pointer.next

    def pop(self) -> Node:
        node = self.head
        self.head = node.next
        return node

    def remove_last(self) -> Node:
        pointer = self.head
        node = self.tail
        while True:
            if pointer.next is self.tail:
                pointer.next = None
                self.tail = pointer
                return node
            pointer = pointer.next

    def remove(self, after: Node) -> None:
        pointer = self.head
        while True:
            if pointer.next is after:
               pointer.next = after.next
               return None

    def len(self) -> int:
        pointer = self.head
        counter = 0
        while pointer is not None:
            counter += 1
            pointer = pointer.next
        return counter


mojaLista = LinkedList()
mojaLista.append(4)
mojaLista.push(3)
mojaLista.push(3)
mojaLista.append(3)
mojaLista.push(3)
mojaLista.append(6)


print(mojaLista)
print(mojaLista.len())
