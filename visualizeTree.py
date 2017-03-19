import pygraphviz as pgz

# from BinarySearchTree import BinarySearchTree
from AVLTree import AVLTree

G = pgz.AGraph()


class avlTree(AVLTree):
    def __iter__(self):
        if self.size > 0:
            min = self.find_min(self.root)
            while min:
                yield min
                min = self.find_successor(min)


def visual_tree():
    for node in bst:
        if node.leftChild:
            G.add_edge(node.key, node.leftChild.key)
        if node.rightChild:
            G.add_edge(node.key, node.rightChild.key)
    G.layout(prog='dot')
    G.draw('tree.png')


if __name__ == '__main__':
    bst = avlTree()
    bst[3] = 'a'
    bst[2] = 'a'
    bst[5] = 'a'
    bst[1] = 'a'
    bst[4] = 'a'
    bst[6] = 'a'
    bst[3.5] = 'a'
    del bst[1]

    visual_tree()
