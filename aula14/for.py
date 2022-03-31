a = [1,2,3,4,5]

for elemento in a:
    print(elemento)

# enumerate

for (indice, elemento) in enumerate(a):
    print(f'{indice} - {elemento}')

# for - else

for (indice, elemento) in enumerate(a):
    print(f'{indice} - {elemento}')
else:
    print('Acabou o for')