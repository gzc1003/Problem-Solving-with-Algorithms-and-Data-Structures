def iqsort(alist):
    qsort_helper(alist, 0, len(alist)-1)

def qsort_helper(alist, start, end):
    if start < end:
        if (end-start)+1 < 4:
            insertionsort(alist,start,end)
        else:
            mid = (start+end)//2
            one = alist[start]
            two = alist[mid]
            three = alist[end]

            if (one-two) * (one-three) <= 0:
                pass
            elif (two-one) * (two-three) <= 0:
                alist[start],alist[mid] = two,one
            else:
                alist[start],alist[end] = three,one

            pivot_value = alist[start]
            leftmark = start + 1
            rightmark = end

            while leftmark <= rightmark:

                while leftmark <= end and alist[leftmark] <= pivot_value:
                    leftmark += 1

                while rightmark > start and alist[rightmark] >= pivot_value:
                    rightmark -= 1

                if leftmark <= rightmark:
                    alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

            alist[start], alist[rightmark] = alist[rightmark], alist[start]
            split_point = rightmark

            qsort_helper(alist, start, split_point-1)
            qsort_helper(alist, split_point+1, end)


def insertionsort(alist,start,end):
    for i in range(start+1, end+1):
        position = i
        currentvalue = alist[i]
        while position > start and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1
        alist[position] = currentvalue


alist = [54,26,93,17,77,31,44,55,20]
iqsort(alist)
print(alist)