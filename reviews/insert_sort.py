def insert_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        for j in range(i,-1,-1):
            if j > 0 and array[j-1] > current_value:
                array[j] = array[j-1]
            else:
                array[j] = current_value
                break

    return array


# def insert_sort(array):
#     for i in range(1, len(array)):
#         current_value = array[i]
#         current = i
#         while current > 0 and array[current-1] > current_value:
#             array[current] = array[current-1]
#             current -= 1
#         array[current] = current_value
#     return array

assert(insert_sort([3,2,6,1,3,3]) == sorted([3,2,6,1,3,3]))