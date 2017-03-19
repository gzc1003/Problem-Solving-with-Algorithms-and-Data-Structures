def revKnap(itemlist, weight):
    if len(itemlist) == 0 and weight > 0:
        return False
    elif weight == 0:
        return True
    else:
        available_itemlist = [item for item in itemlist if item <= weight]
        if len(available_itemlist) == 0:
            return False
        else:
            for i in available_itemlist:
                new_itemlist = itemlist[:]
                new_itemlist.remove(i)
                if revKnap(new_itemlist, weight-i):
                    print('put item: %d in the knapsack' % i)
                    return True


revKnap([1,10,3,6], 10)