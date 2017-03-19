import random

goal = 'methinks it is like a weasel'


def gen_str(strlen):
    string = ''
    for i in range(strlen):
        string += random.choice('abcdefghijklmnopqrstuvwxyz ')
    # print(string)
    return string


def cal_score(string):
    cmp = list(map(lambda a, b: int(a == b), string, goal))
    # print(cmp)
    return cmp.count(1)/len(cmp)


def repeat():
    score = 0
    count = 0
    while score != 1.0:
        tmp_string = gen_str(len(goal))
        tmp_score = cal_score(tmp_string)
        if tmp_score > score:
            score = tmp_score
            res = tmp_string
        count += 1
        if count % 1000 == 0:
            print('%dth: score=%s, string=%s' % (count, score, res))

    return res

repeat()
