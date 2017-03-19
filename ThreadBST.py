from BinarySearchTree import BinarySearchTree, Node


class ThreadedNode(Node):
    def __init__(self, key, val, parent=None,
                 leftchild=None, rightchild=None, righthread=False):
        super().__init__(key, val, parent, leftchild, rightchild)
        self.rightThread = righthread


class ThreadedBST(BinarySearchTree):
    def put(self, key, val):
        if self.root is None:
            self.root = ThreadedNode(key, val)
        else:
            self._put(key, val, self.root)
        self.size += 1

    def _put(self, key, val, currentnode):
        if key == currentnode.key:
            currentnode.payload = val
        elif key > currentnode.key:
            if not currentnode.rightChild or currentnode.rightThread:
                currentnode.rightThread = False
                currentnode.rightChild = ThreadedNode(key, val, currentnode)
                tmp = self.find_successor(currentnode.rightChild)
                if tmp:
                    currentnode.rightChild.rightThread = True
                    currentnode.rightChild.rightChild = tmp
            else:
                self._put(key, val, currentnode.rightChild)
        else:
            if not currentnode.leftChild:
                currentnode.leftChild = ThreadedNode(key, val, currentnode)
                tmp = self.find_successor(currentnode.leftChild)
                if tmp:
                    currentnode.leftChild.rightThread = True
                    currentnode.leftChild.rightChild = tmp
            else:
                self._put(key, val, currentnode.leftChild)

    def __iter__(self):
        if self.size > 0:
            currentnode = self.find_min(self.root)
            yield currentnode.key
            while currentnode.rightThread or currentnode.rightChild:
                if currentnode.rightThread:
                    currentnode = currentnode.rightChild
                else:
                    currentnode = self.find_min(currentnode.rightChild)
                yield currentnode.key

if __name__ == '__main__':

    bst = ThreadedBST()
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

    for key in bst:
        print(key)


