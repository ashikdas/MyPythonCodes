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

