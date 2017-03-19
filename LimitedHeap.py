class BinaryHeap:
    def __init__(self, maxsize):
        self.heap = [0]
        self.size = 0
        self.maxsize = maxsize

    def build_heap(self, alist):
        self.size = len(alist)
        self.heap.extend(alist)
        i = self.size // 2
        while i > 0:
            self.percolate_down(i)
            i -= 1

    def insert(self, k):
        if self.size < self.maxsize:
            self.heap.append(k)
            self.size += 1
            i = self.size
            while i // 2 > 1:
                if self.heap[i] < self.heap[i // 2]:
                    self.heap[i // 2], self.heap[i] = (
                        self.heap[i], self.heap[i // 2])
                    i //= 2
                else:
                    break
        elif self.size == self.maxsize:
            if k > self.heap[1]:
                self.heap[1] = k
                self.percolate_down(1)

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
                self.heap[i], self.heap[re] = (
                    self.heap[re], self.heap[i]
                )
                i = re
            else:
                break

    def min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        elif self.heap[i * 2] <= self.heap[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1


if __name__ == '__main__':
    h = BinaryHeap(5)
    h.build_heap([5,9,8,20])
    print(h.heap)
    print(h.size)
    h.insert(21)
    print(h.heap)
    print(h.size)
    h.insert(10)
    print(h.heap)
    print(h.size)
