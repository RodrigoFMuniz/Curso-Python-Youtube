from functools import reduce
# lambda
l1 = [1,2,3,4,5]

a = lambda x: x**2
print(a(6))

#lambda em map
b = map(lambda x: x**2, l1)

for it in b:
    print(it)


#lambda em reduce
c = reduce(lambda total, x : total + x, l1, 0)
print('Total do reduce: ', c)
