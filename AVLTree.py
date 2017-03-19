from BinarySearchTree import BinarySearchTree, Node


def height(node):
    if node:
        return node.height
    else:
        return -1


def update_height(node):
    node.height = 1 + max(height(node.leftChild), height(node.rightChild))


class AVLNode(Node):
    def __init__(self, key, value, parent=None, leftChild=None,
                 rightChild=None):
        super().__init__(key, value, parent, leftChild, rightChild)
        self.height = 0


class AVLTree(BinarySearchTree):
    def put(self, key, val):
        if self.root is None:
            self.root = AVLNode(key, val)
        else:
            self._put(key, val, self.root)
        self.size += 1

    def _put(self, key, val, currentnode):
        if key > currentnode.key:
            if not currentnode.rightChild:
                currentnode.rightChild = AVLNode(key, val, currentnode)
                self.rebalance(currentnode.rightChild)
            else:
                self._put(key, val, currentnode.rightChild)
        else:
            if not currentnode.leftChild:
                currentnode.leftChild = AVLNode(key, val, currentnode)
                self.rebalance(currentnode.leftChild)
            else:
                self._put(key, val, currentnode.leftChild)

    def rebalance(self, node):
        while node is not None:
            update_height(node)
            if height(node.rightChild) - height(node.leftChild) >= 2:
                if height(node.rightChild.leftChild) > height(node.rightChild.rightChild):
                    self.rightrotate(node.rightChild)
                    self.leftrotate(node)
                else:
                    self.leftrotate(node)
            elif height(node.leftChild) - height(node.rightChild) >= 2:
                if height(node.leftChild.rightChild) > height(node.leftChild.leftChild):
                    self.leftrotate(node.leftChild)
                    self.rightrotate(node)
                else:
                    self.rightrotate(node)

            node = node.parent

    def leftrotate(self, rotroot:AVLNode):
        newroot = rotroot.rightChild
        newroot.parent = rotroot.parent
        if rotroot.parent:
            if rotroot.isrightchild():
                rotroot.parent.rightChild = newroot
            else:
                rotroot.parent.leftChild = newroot
        else:
            self.root = newroot

        rotroot.rightChild = newroot.leftChild
        if rotroot.rightChild is not None:
            newroot.leftChild.parent = rotroot
        newroot.leftChild = rotroot
        rotroot.parent = newroot

        update_height(newroot)
        update_height(rotroot)

    def rightrotate(self, rotroot:AVLNode):
        newroot = rotroot.leftChild
        newroot.parent = rotroot.parent
        if rotroot.parent:
            if rotroot.isrightchild():
                rotroot.parent.rightChild = newroot
            else:
                rotroot.parent.leftChild = newroot
        else:
            self.root = newroot

        rotroot.leftChild = newroot.rightChild
        if rotroot.leftChild is not None:
            newroot.leftChild.parent = rotroot
        newroot.rightChild = rotroot
        rotroot.parent = newroot

        update_height(newroot)
        update_height(rotroot)

    def remove(self, node: Node):
        if not node.leftChild and not node.rightChild:
            if node.isleftchild():
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None
            self.rebalance(node.parent)

        elif node.leftChild and not node.rightChild:
            if node.parent is None:
                node.leftChild.parent = None
                self.root = node.leftChild
            elif node.isleftchild():
                node.leftChild.parent = node.parent
                node.parent.leftChild = node.leftChild
            else:
                node.leftChild.parent = node.parent
                node.parent.rightChild = node.leftChild
            self.rebalance(node.parent)

        elif node.rightChild and not node.leftChild:
            if node.parent is None:
                node.rightChild.parent = None
                self.root = node.rightChild
            elif node.isleftchild():
                node.rightChild.parent = node.parent
                node.parent.leftChild = node.rightChild
            else:
                node.rightChild.parent = node.parent
                node.parent.rightChild = node.rightChild
            self.rebalance(node.parent)

        else:
            successor = self.find_successor(node)
            node.key = successor.key
            node.payload = successor.payload
            self.remove(successor)


if __name__ == '__main__':

    avl = AVLTree()
    avl[1] = 'a'
    avl[2] = 'a'
    avl[3] = 'a'
    avl[4] = 'a'
    print(height(avl.root))

