lista = [1,2,3,4,5,6,7,8]
var1,*var2,var3 = lista
print(var1)
print(var2)
print(var3)

dic1 = {'var 1':'value 1', 'var 2':'value 2','var 3':'value 3','var 4':'value 4'}
d1, d2, *d3 = dic1
print(d1)
print(d2)
print(d3)

dic2 = {'var 1':'value 1', 'var 2':'value 2','var 3':'value 3','var 4':'value 4'}
d4, d5, *d6 = dic2.items()
print(d4)
print(d5)
print(d6)

dic3 = {'var 1':'value 1', 'var 2':'value 2','var 3':'value 3','var 4':'value 4'}
d7, d8, *d9 = dic2.values()
print(d7)
print(d8)
print(d9)

# para ignorar items da desestruturação, usar _
dic3 = {'var 1':'value 1', 'var 2':'value 2','var 3':'value 3','var 4':'value 4'}
_, d10, *_ = dic2.items()
print(d10)
print(_)