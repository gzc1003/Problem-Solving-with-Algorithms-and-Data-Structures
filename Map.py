class Map:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.length = 0

    def __len__(self):
        return self.length

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key,value)

    def __contains__(self, key):
        hashvalue = self.hashfunction(key)
        start = hashvalue
        while self.slots[hashvalue] is not None:
            if self.slots[hashvalue] == key:
                return True
            hashvalue = self.rehash(hashvalue)
            if hashvalue == start:
                break
        return False

    def __delitem__(self, key):
        hashvalue = self.hashfunction(key)
        del_hashvalue = hashvalue
        last_pos = None
        while True:
            hashvalue = self.rehash(hashvalue)
            if self.slots[hashvalue] is None:
                break
            if hashvalue == del_hashvalue:
                break
            next_pos = hashvalue
            nextkey = self.slots[next_pos]
            nexthashvalue = self.hashfunction(nextkey)
            if nexthashvalue == del_hashvalue:
                last_pos = next_pos
        if last_pos:
            self.slots[del_hashvalue] = self.slots[last_pos]
            self.slots[last_pos] = None
            self.data[del_hashvalue] = self.data[last_pos]
            self.data[last_pos] = None
        else:
            self.slots[del_hashvalue] = None
            self.data[del_hashvalue] = None

    def put(self,key,value):

        load_factor = self.length / self.size
        if load_factor > 0.5:
            self.resize(2*self.size)
        self.length += 1
        
        position = self.hashfunction(key)
        replaced = False
        while self.slots[position] is not None:
            if self.slots[position] == key:
                self.data[position] = value
                replaced = True
                break
            position = self.rehash(position)

        if not replaced:
            self.slots[position] = key
            self.data[position] = value

    def get(self,key):
        hashvalue = self.hashfunction(key)
        start = hashvalue
        while self.slots[hashvalue] is not None:
            if self.slots[hashvalue] == key:
                break
            hashvalue = self.rehash(hashvalue)
            if hashvalue == start:
                return None
        return self.data[hashvalue]


    def hashfunction(self,key):
        return key % self.size

    def rehash(self,pos):
        return (pos+1) % self.size

    def resize(self,newsize):

        oldsize = self.size
        oldslot = self.slots
        olddata = self.data

        self.size = newsize
        self.slots = [None] * newsize
        self.data = [None] * newsize

        self.length = 0

        for i in range(oldsize):
            if oldslot[i] is not None:
                self.put(oldslot[i], olddata[i])


H=Map()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
print(len(H))

print(H[20])

print(H[17])
H[20]='duck'
print(H[20])
print(H[99])
print(H.data)
print(99 in H)
print(20 in H)
del H[77]
print(55 in H)
print(H[44])