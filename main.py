from typing import Any, List, Callable, Union


class TreeNode:
    value: Any
    kids = List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.kids = []

    def __str__(self):
        if self.isLeaf():
            return f'Node: {self.value}'

        kidsString = ''
        for i in range(len(self.kids)):
            kidsString += f'{self.kids[i].value}, ' if i < len(self.kids) - 1 else f'{self.kids[i].value}'

        return f'Node: {self.value}, kids: {kidsString}'

    def isLeaf(self):
        return len(self.kids) == 0

    def add(self, kid: 'TreeNode'):
        self.kids.append(kid)

    def forEachDeepFirst(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for k in self.kids:
            visit(k)

    def forEachLevelOrder(self, visit: Callable[['TreeNode'], None]) -> None:
        queue = [self]
        while len(queue) > 0:
            node = queue.pop()
            visit(node)
            for k in node.kids:
                queue.append(k)

    def search(self, value: Any) -> List['TreeNode']:
        list = []

        def func_custom(treeNode: TreeNode):
            if treeNode.value == value:
                list.append(treeNode)

        self.forEachDeepFirst(func_custom)

        return list


class Tree:
    root: TreeNode

    # def add(self, value: Any, parent: TreeNode):
