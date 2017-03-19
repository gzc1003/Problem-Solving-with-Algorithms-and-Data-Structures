def qsort(array):
    qsort_helper(0, len(array)-1, array)
    return array

def qsort_helper(start, end, array):
    if start >= end: return

    split = patition(start,end,array)
    qsort_helper(start, split-1, array)
    qsort_helper(split+1, end, array)


def patition(start, end, array):
    pivot_value = array[start]
    left = start + 1
    right = end
    while True:
        while left <= right and array[left] <= pivot_value:
            # left <= right很重要
            # 1. 防止pivot为最大或最小值时，数组越界
            # 2. 防止包含很多重复元素的数组，时间复杂度变为O(N^2)
            # 诸如：[3,3,3,3,4,5,6]
            left = left + 1

        while left <= right and array[right] >= pivot_value:
            right = right -1

        if left > right:
            break
        else:
            tmp = array[left]
            array[left] = array[right]
            array[right] = tmp

    array[start] = array[right]
    array[right] = pivot_value

    return right

assert(qsort([3,5,1,2,7,6,3,3]) == sorted([3,5,1,2,7,6,3,3]))
assert(qsort([3,3,3,3,3,3,3,3]) == sorted([3,3,3,3,3,3,3,3]))
assert(qsort([3,3,3,3,7,6,8,9]) == sorted([3,3,3,3,7,6,8,9]))
assert(qsort([6,3,5,4,6,6,6,6]) == sorted([6,3,5,4,6,6,6,6]))
