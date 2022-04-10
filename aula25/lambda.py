# lambda
a = lambda x: x**2
print(a(6))

#lambda em map
l1 = [1,2,3,4,5]

b = map(lambda x: x**2, l1)

for it in b:
    print(it)