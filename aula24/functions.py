# functions

def sum(*v):
    total = 0
    for n in v[0]:
        total +=  n
    return total

values = [1,2,3,4,5,6,7,8,9,10]

print(sum(values))