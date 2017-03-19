from maxHeap import BinaryHeap


class SortHeap(BinaryHeap):
    def del_max(self):
        self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
        self.size -= 1
        self.percolate_down(1)


def heap_sort(alist):
    MaxHeap = SortHeap()
    MaxHeap.build_heap(alist)
    for i in range(len(alist)):
        MaxHeap.del_max()
    MaxHeap.heap.pop(0)
    return MaxHeap.heap


alist1 = []
alist2 = [1]
alist3 = [5,8,3,10,23,90,45]
alist4 = [2,2,3]
alist5 = [5,5]

print(heap_sort(alist1))
print(heap_sort(alist2))
print(heap_sort(alist3))
print(heap_sort(alist4))
print(heap_sort(alist5))