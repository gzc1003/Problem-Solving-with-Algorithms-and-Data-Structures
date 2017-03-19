class BinaryHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def build_heap(self, alist):
        self.size = len(alist)
        self.heap.extend(alist)
        i = self.size // 2
        while i > 0:
            self.percolate_down(i)
            i -= 1

    def insert(self, k):
        self.heap.append(k)
        self.size += 1
        i = self.size
        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                self.heap[i // 2], self.heap[i] = (
                    self.heap[i], self.heap[i // 2])
                i //= 2
            else:
                break

    def del_max(self):
        re = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        if self.size:
            self.percolate_down(1)
        return re

    def percolate_down(self, i):
        while i * 2 <= self.size:
            re = self.max_child(i)
            if self.heap[re] > self.heap[i]:
                self.heap[i], self.heap[re] = (
                    self.heap[re], self.heap[i]
                )
                i = re
            else:
                break

    def max_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        elif self.heap[i * 2] >= self.heap[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1


if __name__ == '__main__':
    bh = BinaryHeap()
    bh.build_heap([2, 3, 5, 6, 9])
    print(bh.heap)
    print(bh.del_max())
    print(bh.del_max())
    print(bh.del_max())
    print(bh.del_max())
    print(bh.del_max())
