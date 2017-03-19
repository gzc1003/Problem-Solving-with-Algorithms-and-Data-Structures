def mergesort(alist):
    mergesort_helper(alist, 0, len(alist)-1)


def mergesort_helper(alist, start, end):

    if start < end:
        mid = (end+start) // 2
        mergesort_helper(alist,start,mid)
        mergesort_helper(alist,mid+1,end)

        leftlist = []
        for i in range(start, mid+1):
            leftlist.append(alist[i])

        rightlist = []
        for j in range(mid+1, end+1):
            rightlist.append(alist[j])

        i = 0
        j = 0
        k = start
        while i < len(leftlist) and j < len(rightlist):
            if leftlist[i] < rightlist[j]:
                alist[k] = leftlist[i]
                i += 1
                k += 1
            else:
                alist[k] = rightlist[j]
                j += 1
                k += 1
        while i < len(leftlist):
            alist[k] = leftlist[i]
            i += 1
            k += 1
        while j < len(rightlist):
            alist[k] = rightlist[j]
            j += 1
            k += 1


alist = [54,26,93,17,77,31,44,55,20]
mergesort(alist)
print(alist)