from BinaryTreePrinter import BinaryTreePrinter
from stack import Queue


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            nodes = Queue()
            nodes.enqueue(self.root)

            while True:
                checking_node = nodes.dequeue()
                if checking_node.left is None:
                    checking_node.left = TreeNode(val)
                    return
                elif checking_node.right is None:
                    checking_node.right = TreeNode(val)
                    return
                else:
                    nodes.enqueue(checking_node.left)
                    nodes.enqueue(checking_node.right)

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)


class BST:
    def __init__(self):
        self.root = None

    def __insert_value(self, node, value):
        if node is None:
            return

        if node.val == value:
            return
        elif value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
                return
            self.__insert_value(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
                return
            self.__insert_value(node.right, value)

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.__insert_value(self.root, val)

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)

# my_tree = BinaryTree()
# # for c in ['a', 'b', 'c', 'd']:
# #     my_tree.insert(c)
# #     print(my_tree)
# my_tree.insert('a')
# print(my_tree)

bst = BST()
for i in [8, 5, 3, 2, 9, 23,76,50,1]:
    bst.insert(i)
    print(bst)