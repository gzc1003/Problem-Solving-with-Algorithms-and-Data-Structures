def shellsort(alist):
    sublist = len(alist)//2
    while sublist > 0:
        for start in range(sublist):
            gap = sublist
            insertionsort(alist,start,gap)

        sublist = sublist//2



def insertionsort(alist,start,gap):

    for i in range(start+gap,len(alist),gap):
        position = i
        currentvalue = alist[position]
        while currentvalue < alist[position-gap] and position > start:
            alist[position] = alist[position-gap]
            position -= gap
        alist[position] = currentvalue


alist = [54,26,93,17,77,31,44,55,20]
shellsort(alist)
print(alist)