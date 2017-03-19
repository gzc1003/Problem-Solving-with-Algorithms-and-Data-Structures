def makechangeDP(change, coinlist, mincoinsmatrix):
    coinlist.sort()
    for coin in coinlist:
        row = coinlist.index(coin)
        for chng in range(change+1):
            if row == 0:
                mincoinsmatrix[row][chng] = chng
            elif coin > chng:
                mincoinsmatrix[row][chng] = mincoinsmatrix[row-1][chng]
            else:
                mincoinsmatrix[row][chng] = min(mincoinsmatrix[row][chng-coin]+1,
                                              mincoinsmatrix[row-1][chng])
    print(mincoinsmatrix[row][chng])
    while chng>0:
        if row == 0 or mincoinsmatrix[row][chng] < mincoinsmatrix[row-1][chng]:
            print('give back %d' % coinlist[row])
            chng -= coinlist[row]
        else:
            row -= 1


def initialize(row, column):
    matrix = []
    for i in range(row):
        tmp = [0 for j in range(column)]
        matrix.append(tmp)
    return matrix


change = 2
coinlist = [1,5,10,21,25]

mincoinsmatrix = initialize(len(coinlist), change+1)

makechangeDP(change, coinlist, mincoinsmatrix)