import timeit

class Node:
    def __init__(self,item):
        self.data = item
        self.next = None
        self.previous = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

    def setPrevious(self,pre):
        self.previous = pre


class UnorderedList:

    def __init__(self):
        self.head = None
        self.end = None
        self.length = 0

    def isEmpty(self):
        return self.head == None

    def size(self):
        return self.length

    def add(self,item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            self.end = temp
        else:
            self.head.setPrevious(temp)
            temp.setNext(self.head)
            self.head = temp
        self.length += 1

    def pop(self):
        res = self.end.getData()
        pre = self.end.getPrevious()
        if pre is None:
            self.head = None
            self.end = None
        else:
            pre.setNext(None)
            self.end = pre

        self.length -= 1
        return res

    def __str__(self):
        current = self.head
        res = "["
        while current is not None:
            item = current.getData()
            if current.getNext() is None:
                res += str(item)+']'
            else:
                res += str(item)+', '
            current = current.getNext()
        return res

for i in range(1000000, 10000001, 1000000):
    t = timeit.Timer("mylist.pop()",
                     "from __main__ import mylist")
    mylist = list(range(i))
    pylist_time = t.timeit(1000)
    mylist = UnorderedList()
    for j in range(i):
        mylist.add(i)
    mylist_time = t.timeit(1000)
    print("%d\tpylist: %10.6f\tmylist: %10.6f" %
          (i,pylist_time,mylist_time))

