class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None
        self.end = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            self.end = temp
        else:
            temp.setNext(self.head)
            self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        elif current == self.end:
            self.end = previous
            previous.setNext(current.getNext())
        else:
            previous.setNext(current.getNext())

    def append(self,item):
        list_end = self.end
        temp = Node(item)
        if list_end is None:
            self.head = temp
            self.end = temp
        else:
            list_end.setNext(temp)
            self.end = temp

    def index(self,item):
        current = self.head
        ordinal = 0
        found = False
        while not found:

            if item == current.getData():
                found = True
            else:
                current = current.getNext()
                ordinal += 1
        return ordinal

    def insert(self,pos,item):
        temp = Node(item)

        index = 0
        current =self.head
        previous = None
        found = False
        while current is not None and not found:
            if index == pos:
                found = True
            else:
                previous = current
                current = current.getNext()
                index += 1
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        elif index == pos:
            self.append(item)
        else:
            temp.setNext(current)
            previous.setNext(temp)


    def pop(self, pos=None):
        if pos is None:
            res = self.end.getData()
            self.remove(res)
        else:
            index = 0
            current = self.head
            previous = None
            found = False
            while not found:
                if index == pos:
                    found = True
                else:
                    current = current.getNext()
                    index += 1
            res = current.getData()
            self.remove(res)
        return res

mylist = UnorderedList()
mylist.add(1)
mylist.remove(1)
print(mylist.size())