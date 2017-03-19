import timeit


for i in range(10000,100001,20000):
    t = timeit.Timer("del x[k];k+=1",
                     "from __main__ import x,k")
    x = {j: None for j in range(i)}
    k=0
    dict_del_time = t.timeit(number=1000)
    x = list(range(i))
    k=0
    lst_del_time = t.timeit(number=1000)
    print('%d\t%10.6f\t%10.6f' % (i, dict_del_time, lst_del_time))
