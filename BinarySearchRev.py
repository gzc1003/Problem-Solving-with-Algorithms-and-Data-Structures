def binary_search(alist, item):
    return binary_search_helper(alist, item, 0, len(alist)-1)

def binary_search_helper(alist, item, start, end):
    if start > end:
        return False
    else:
        midpoint = (start + end) // 2
        if item == alist[midpoint]:
            return True
        elif item > alist[midpoint]:
            start = midpoint+1
            return binary_search_helper(alist, item, start, end)
        else:
            end = midpoint-1
            return binary_search_helper(alist, item, start, end)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
