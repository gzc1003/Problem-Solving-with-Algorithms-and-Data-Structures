class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, newnode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insert_right(self, newnode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def get_right_child(self):
        return self.rightChild

    def get_left_child(self):
        return self.leftChild

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key

    def __iter__(self):
        if self:
            if self.leftChild:
                for key in self.leftChild:
                    yield key
            yield self.key
            if self.rightChild:
                for key in self.rightChild:
                    yield key

if __name__ == '__main__':
    BT = BinaryTree(3)
    BT.insert_left(1)
    BT.insert_right(5)
    for key in BT:
        print(key)

