class MaxHeap(object):
    def __init__(self):
        self.size = 0
        self.heap = [0]

    def build_heap(self, alist):
        self.heap += alist
        self.size = len(alist)
        i = self.size // 2
        while i > 0:
            self._sink(i)
            i = i - 1

    def _sink(self, i):
        while 2 * i <= self.size:
            left = 2*i
            right = left+1
            j = i
            if left <= self.size and self.heap[left] > self.heap[j]:
                j = left
            if right <= self.size and self.heap[right] > self.heap[j]:
                j = right
            if j == i: break
            self.heap[j], self.heap[i] = self.heap[i], self.heap[j]
            i = j

    def insert(self, key):
        self.size += 1
        self.heap.append(key)
        self._swim(self.size)

    def _swim(self, i):
        while i > 1 and self.heap[i] > self.heap[i//2]:
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i // 2

    def del_max(self):
        res = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self._sink(1)

        return res

    def max(self):
        return self.heap[1]

    def heap_sort(self):
        while self.size > 1:
            self.heap[self.size], self.heap[1] = \
                self.heap[1], self.heap[self.size]
            self.size -= 1
            self._sink(1)



heap = MaxHeap()
heap.build_heap([8,10,5,7,8,8,3])
heap.heap_sort()
print(heap.heap)