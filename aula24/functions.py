# functions

from functools import reduce


def sum(*v):
    total = 0
    for n in v[0]:
        total +=  n
    return total

def sum2(*v):
    return reduce(lambda a,x: a+x,v[0],0)

values = [1,2,3,4,5,6,7,8,9,10,11]

print(sum(values))
print(sum2(values))