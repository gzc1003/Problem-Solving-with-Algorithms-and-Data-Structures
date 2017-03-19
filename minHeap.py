class minHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, node):
        self.heap.append(node)
        self.size += 1
        self.percolate_up(self.size)

    def percolate_up(self, i):
        while i > 1:
            if self.heap[i//2] > self.heap[i]:
                self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
                i //= 2
            else:
                break

    def del_min(self):
        re = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.percolate_down(1)
        return re

    def percolate_down(self, i):
        while i * 2 <= self.size:
            re = self.min_child(i)
            if self.heap[re] < self.heap[i]:
                self.heap[i], self.heap[re] = self.heap[re], self.heap[i]
                i = re
            else:
                break

    def min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        elif self.heap[i * 2] < self.heap[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    def build_heap(self, alist):
        self.heap.extend(alist)
        self.size = len(alist)
        i = self.size // 2
        while i > 0:
            self.percolate_down(i)
            i -= 1

    def decrease_key(self, vertex, distance):
        i = 1
        for vert in self.heap[1:]:
            if vertex == vert[1]:
                self.heap[i] = (distance, vertex)
                self.percolate_up(i)
            i += 1

    def __contains__(self, item):
        return item in self.heap


