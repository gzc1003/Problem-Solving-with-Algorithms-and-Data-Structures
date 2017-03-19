def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
        sorted = True
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                sorted = False
        if sorted: break
    return array

assert(bubble_sort([3,2,6,1,3,3]) == sorted([3,2,6,1,3,3]))