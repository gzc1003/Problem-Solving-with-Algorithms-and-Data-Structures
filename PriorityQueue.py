from maxHeap import BinaryHeap


class PriorityQueue(BinaryHeap):
    def dequeue(self):
        return self.del_max()

    def enqueue(self, k):
        self.insert(k)

    def __str__(self):
        return str(self.heap[1:])

if __name__ == '__main__':
    PQ = PriorityQueue()
    print(PQ)
    PQ.enqueue(3)
    PQ.enqueue(9)
    PQ.enqueue(10)
    print(PQ)
    item = PQ.dequeue()
    print(item)
    print(PQ)
    print(PQ.size)

