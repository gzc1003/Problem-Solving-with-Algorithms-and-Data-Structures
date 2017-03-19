def doubly_bubble(alist):
    doubly_bubble_helper(alist, 0, len(alist)-1)

def doubly_bubble_helper(alist, start, end):
    for passtime in range(len(alist)-1):

        exchanged = False

        if passtime%2 == 0:
            for j in range(start,end):
                if alist[j] > alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
                    exchanged = True
            end -= 1
        else:
            for j in range(end,start,-1):
                if alist[j] < alist[j-1]:
                    alist[j-1], alist[j] = alist[j], alist[j-1]
                    exchanged = True
            start += 1

        if not exchanged:
            break

alist=[20,30,40]
doubly_bubble(alist)
print(alist)
