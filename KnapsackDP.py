def knapDP(weight, itemlist, maxvaluematrix):
    for item in itemlist:
        item_weight = weightlist[item]
        item_value = valuelist[item]
        for w in range(weight+1):
            if item_weight > w:
                maxvaluematrix[item][w] = maxvaluematrix[item-1][w]
            else:
                maxvaluematrix[item][w] = max(maxvaluematrix[item-1][w-item_weight]+item_value,
                                              maxvaluematrix[item-1][w])
    print(maxvaluematrix[item][w])
    while w>0:
        if maxvaluematrix[item][w] > maxvaluematrix[item-1][w]:
            print('put item %d in knapsack' % item)
            w -= weightlist[item]
            item -= 1
        else:
            item -= 1


def initialize(row, column):
    matrix = []
    for i in range(row):
        tmp = [0 for j in range(column)]
        matrix.append(tmp)
    return matrix


knap_capacity = 2
itemlist = [1,2,3,4,5]
weightlist = [0,3,2,4,5,9]
valuelist = [0,3,4,8,8,10]

maxvaluematrix = initialize(len(itemlist)+1, knap_capacity+1)

knapDP(knap_capacity, itemlist, maxvaluematrix)






