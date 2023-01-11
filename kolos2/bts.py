class Node:
    data: int
    left: 'Node'
    right: 'Node'

    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None

    def child_count(self) -> int:
	    count = 0
	    if self.left:
		    count += 1
	    if self.right:
		    count += 1
	    return count


class Tree:
    root: Node

    def __init__(self):
        self.root = None

    def print(self) -> None:
        if self.root is None:
            print('Tree is empty')
            return

        pointer = self.root

        while True:
            print(pointer.data)

            if pointer.child_count() == 2:
                direction = input('a/d: ')
                if direction == 'a':
                    pointer = pointer.left
                else:
                    pointer = pointer.right
                continue
            elif pointer.child_count() == 1:
                if pointer.left:
                    print('going left')
                    pointer = pointer.left
                else:
                    print('going right')
                    pointer = pointer.right
                continue
            else:
                break

    # return parent of "node with value {data}" and this node
    # if parent is None it means "node with value {data}" is root
    def get_parent_by_value(self, data: int) -> (Node, Node):  # parent, child with value 'data'
        if self.root.data == data:
            return None, self.root

        pointer = self.root

        while True:
            if pointer is None:
                return None, None

            if pointer.left and pointer.left.data == data:
                return pointer, pointer.left
            if pointer.right and pointer.right.data == data:
                return pointer, pointer.right

            if data < pointer.data:
                pointer = pointer.left
            else:
                pointer = pointer.right

    def get_parent_of_leftest(self, node: Node) -> Node:
        pointer = node

        while pointer.left.left:
            pointer = pointer.left

        return pointer

    def add(self, data: int) -> None:
        if self.root is None:
            self.root = Node(data)
            return

        pointer = self.root

        while True:
            if data < pointer.data:  # going left
                if pointer.left is not None:  # check if left is not empty
                    pointer = pointer.left
                    continue
                else:
                    pointer.left = Node(data)
                    return
            else:  # data >= pointer.data
                if pointer.right is not None:
                    pointer = pointer.right
                    continue
                else:
                    pointer.right = Node(data)
                    return

    def remove(self, data: int) -> None:
        parent, node_to_remove = self.get_parent_by_value(data)

        if node_to_remove is None:
            print('There is no node with given value')
            return

        child_count = node_to_remove.child_count()

        if child_count == 0:
            if parent is None:
                self.root = None
            elif parent.left is node_to_remove:
                parent.left = None
            else: # parent.right is child
                parent.right = None
            return

        if child_count == 1:
            # if node_to_remove.left is not None:
            #     child_of_child = node_to_remove.left
            # else:
            #     child_of_child = node_to_remove.right

            child_of_child = node_to_remove.left if node_to_remove.left is not None else node_to_remove.right

            if parent is None:
                self.root = child_of_child
            elif parent.left is node_to_remove:
                parent.left = child_of_child
            else:  # parent.right is node_to_remove
                parent.right = child_of_child
            return

        if child_count == 2:  # redundant
            right_child_of_removed = node_to_remove.right

            if right_child_of_removed.left is None:

                if parent is None:
                    self.root = right_child_of_removed
                elif parent.left is node_to_remove:
                    parent.left = right_child_of_removed
                else:  # parent.right is node_to_remove
                    parent.right = right_child_of_removed

                right_child_of_removed.left = node_to_remove.left

            else:  # right_child_of_removed has left child

                parent_of_leftest = self.get_parent_of_leftest(right_child_of_removed)

                new_node = parent_of_leftest.left
                parent_of_leftest.left = None

                if parent is None:
                    self.root = new_node
                elif parent.left is node_to_remove:
                    parent.left = new_node
                else:  # parent.right is node_to_remove
                    parent.right = new_node

                new_node.left = node_to_remove.left
                new_node.right = node_to_remove.right
