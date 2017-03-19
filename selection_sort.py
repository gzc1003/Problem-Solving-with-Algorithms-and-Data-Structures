def selection_sort(array):
    for i in range(len(array)-1, 0, -1):
        max = 0
        for j in range(1, i+1):
            if array[j] > array[max]:
                max = j
        array[i], array[max] = array[max], array[i]
    return array

assert(selection_sort([3,2,6,1,3,3]) == sorted([3,2,6,1,3,3]))