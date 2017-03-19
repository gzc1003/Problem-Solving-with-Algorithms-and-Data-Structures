def qsort(alist):
    qsort_helper(alist, 0, len(alist)-1)

def qsort_helper(alist, start, end):

    if start < end:
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

            while  alist[rightmark] >= pivot_value and rightmark > start:
                rightmark -= 1

            if leftmark <= rightmark:
                alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

        alist[start], alist[rightmark] = alist[rightmark], alist[start]
        split_point = rightmark

        qsort_helper(alist, start, split_point-1)
        qsort_helper(alist, split_point+1, end)


alist = [3,3,2,3]
qsort(alist)
print(alist)