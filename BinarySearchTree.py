class Node:
    def __init__(self, key, value, parent=None,
                 leftChild=None, rightChild=None):
        self.key = key
        self.payload = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.parent = parent

    def isleftchild(self):
        return self == self.parent.leftChild

    def isrightchild(self):
        return self == self.parent.rightChild

    def __iter__(self):
        if self.leftChild:
            for key in self.leftChild:
                yield key
        yield self.key
        if self.rightChild:
            for key in self.rightChild:
                yield key


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root is None:
            self.root = Node(key, val)
        else:
            self._put(key, val, self.root)
        self.size += 1

    def _put(self, key, val, currentnode):
        if key == currentnode.key:
            currentnode.payload = val
        elif key > currentnode.key:
            if not currentnode.rightChild:
                currentnode.rightChild = Node(key, val, currentnode)
            else:
                self._put(key, val, currentnode.rightChild)
        else:
            if not currentnode.leftChild:
                currentnode.leftChild = Node(key, val, currentnode)
            else:
                self._put(key, val, currentnode.leftChild)

    def get(self, key):
        if self.root:
            node = self._get(key, self.root)
            if node:
                return node.payload
        return None

    def _get(self, key, currentnode):
        if key == currentnode.key:
            return currentnode
        elif key > currentnode.key:
            if not currentnode.rightChild:
                return None
            else:
                return self._get(key, currentnode.rightChild)
        else:
            if not currentnode.leftChild:
                return None
            else:
                return self._get(key, currentnode.leftChild)

    def delete(self, key):
        if self.size > 1:
            node = self._get(key, self.root)
            if node:
                self.remove(node)
                self.size -= 1
            else:
                raise ValueError("Not found the key")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise ValueError("Not found the key")

    def remove(self, node: Node):
        if not node.leftChild and not node.rightChild:
            if node.isleftchild():
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None

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

        else:
            successor = self.find_successor(node)
            node.key = successor.key
            node.payload = successor.payload
            self.remove(successor)

    def find_successor(self, node):
        successor = None
        if node.rightChild:
            successor = self.find_min(node.rightChild)
        elif node.parent:
            if node.isleftchild():
                successor = node.parent

            else:
                node.parent.rightChild = None
                successor = self.find_successor(node.parent)
                node.parent.rightChild = node

        return successor

    def find_min(self, node):
        while node.leftChild is not None:
            node = node.leftChild
        return node

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.delete(key)

    def __iter__(self):
        if self.size > 0:
            min = self.find_min(self.root)
            while min:
                yield min.key
                min = self.find_successor(min)

        # return self.root.__iter__()

if __name__ == '__main__':

    bst = BinarySearchTree()
    bst[30] = 'a'
    bst[20] = 'b'
    bst[10] = 'c'
    bst[40] = 'd'
    bst[50] = 'e'
    bst[35] = 'f'
    bst[25] = 'g'
    bst[28] = 'i'
    bst[26] = 'j'
    bst[34] = 'j'
    bst[33] = 'k'
    bst[23] = 'l'
    bst[23] = 'changed'
    print(bst[23])

    print(bst[10], bst[20], bst[60])
    for key in bst:
        print(key)
    print(len(bst))

    del bst[50]
    del bst[35]
    del bst[20]

    print(len(bst))

    print(bst[50], bst[35], bst[20])
    for key in bst:
        print(key)

    print(len(bst))
    bst[23] = 'changed again'
    print(bst[23], bst[34])

