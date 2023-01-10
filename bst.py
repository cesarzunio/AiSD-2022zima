from typing import Any, Callable


class Node:
    value: int
    left: 'Node'
    right: 'Node'

    def __init__(self, value: int):
        self.value = value
        self.left = self.right = None

    def child_count(self) -> int:
        if self.left:
            if self.right:
                return 2
            return 1
        if self.right:
            return 1
        return 0


class Tree:
    root: Node

    def __init__(self):
        self.root = None

    def print(self) -> None:
        pointer = self.root

        if pointer is None:
            print('Tree is empty')
            return

        while True:
            print(pointer.value)

            child_count = pointer.child_count()
            if child_count == 2:
                check = input('a/d: ')
                if check == 'a':
                    pointer = pointer.left
                    print('going left')
                else:
                    pointer = pointer.right
                    print('going right')
                continue
            elif child_count == 1:
                if pointer.left:
                    pointer = pointer.left
                    print('going left')
                else:
                    pointer = pointer.right
                    print('going right')
                continue
            break

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        pointer = self.root

        while True:
            if value < pointer.value:
                if pointer.left:
                    pointer = pointer.left
                else:
                    pointer.left = Node(value)
                    return
            else:
                if pointer.right:
                    pointer = pointer.right
                else:
                    pointer.right = Node(value)
                    return

    # def insert(self, value: int) -> None:
    #     self.root = self.__insert(self.root, value)
    #
    # def __insert(self, node: Node, value: int) -> Node:
    #     if node is None:
    #         return Node(value)
    #
    #     if value < node.value:
    #         node.left = self.__insert(node.left, value)
    #     else:
    #         node.right = self.__insert(node.right, value)
    #
    #     return node

    def find_parent_by_value(self, node: Node, value: int) -> (Node, Node):
        if node is None or self.root.value == value:
            return None, None

        if node.left and node.left.value == value:
            return node, node.left
        elif node.right and node.right.value == value:
            return node, node.right

        if value < node.value:
            return self.find_parent_by_value(node.left, value)
        else:
            return self.find_parent_by_value(node.right, value)

    def get_parent_smallest(self, node: Node) -> (Node, Node):
        if node.left is None:
            return None, node

        while node.left.left:
            node = node.left
        return node, node.left

    def remove(self, value: int) -> None:
        if self.root is None:
            return None

        if self.root.value == value:
            to_remove_parent = None
            to_remove = self.root
        else:
            to_remove_parent, to_remove = self.find_parent_by_value(self.root, value)

        if to_remove is None:
            print(f'Node with value "{value}" not found')
            return

        child_count = to_remove.child_count()

        if child_count == 0:
            if to_remove_parent is None:
                self.root = None
            elif to_remove_parent.left is to_remove:
                to_remove_parent.left = None
            else:
                to_remove_parent.right = None
            return

        if child_count == 1:
            child = to_remove.left if to_remove.left is not None else to_remove.right

            if to_remove_parent is None:
                self.root = child
            if to_remove_parent.left is to_remove:
                to_remove_parent.left = child
            else:
                to_remove_parent.right = child
            return

        smallest_parent, smallest = self.get_parent_smallest(to_remove.right)

        if to_remove_parent is None:
            self.root = smallest
        elif to_remove_parent.left is to_remove:
            to_remove_parent.left = smallest
        else:
            to_remove_parent.right = smallest

        smallest.left = to_remove.left
        smallest.right = to_remove.right

        if smallest_parent is None:  # prawy nie ma zadnych lewych
            smallest.right = None
        else:
            smallest_parent.left = None

    def contains(self, value: int) -> bool:
        return self.__contains(self.root, value)

    def __contains(self, node: Node, value: int) -> bool:
        if node is None:
            return False

        if node.value == value:
            return True

        if self.__contains(node.left, value):
            return True

        if self.__contains(node.right, value):
            return True

        return False


tree = Tree()
tree.insert(8)
tree.insert(3)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(10)
tree.insert(9)
tree.insert(14)
tree.insert(13)
tree.insert(15)

tree.remove(10)

tree.print()