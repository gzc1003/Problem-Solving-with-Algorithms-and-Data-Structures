def merge_sort(array):
    auxiliary = [0 for i in range(len(array))]
    sort(0, len(array)-1, array, auxiliary)
    return array

def sort(start, end, array, auxiliary_array):
    if start == end: return

    mid = (start + end) // 2
    sort(start, mid, array, auxiliary_array)
    sort(mid+1, end, array, auxiliary_array)
    merge(start, mid, end, array, auxiliary_array)


def merge(start, mid, end, array, auxiliary):
    auxiliary[start:end+1] = array[start:end+1]
    i, j = start, mid+1
    while start <= end:
        if i > mid:
            array[start] = auxiliary[j]
            j += 1
        elif j > end:
            array[start] = auxiliary[i]
            i += 1
        elif auxiliary[i] <= auxiliary[j]:
            array[start] = auxiliary[i]
            i = i+1
        else:
            array[start] = auxiliary[j]
            j = j+1
        start = start + 1
