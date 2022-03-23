# dict

d1 = {'el_1': 'Valor 1'}

print('Dict 1:',d1)
print(dir(d1))

# Update
print('Dict 1 (update) antes:',d1)
print('retorno de update: ', d1.update({'el_2':'Valor 2','el_3': 'Valor 3'}))
print('Dict 1 (update) depois:',d1)

# Get

print('Dict 1 (get) antes:',d1)
print('retorno de Get: ', d1.get('el_2'))
print('retorno de Get: ', d1.get('el_20','Chave não encontrada'))
print('Dict 1 (get) Depois:',d1)

# Pop, Retorna o valor deletado

print('Dict 1 (pop) antes:',d1)
print('retorno de pop: ', d1.pop('el_2'))
print('retorno de pop: ', d1.pop('el_20', 'Retorno default'))
print('Dict 1 (pop) depois:',d1)

# Popitem, Retorna o valor deletado

print('Dict 1 (popitem) antes:',d1)
print('retorno de popitem: ', d1.popitem())
print('Dict 1 (popitem) depois:',d1)

# items

print('Dict 1 (items) antes:',d1)
print('retorno de items: ', d1.items())
print('Dict 1 (items) depois:',d1)

# Values

print('Dict 1 (values) antes:',d1)
print('retorno de values: ', d1.values())
print('retorno de values: ', type(d1.values()))
print('Dict 1 (values) depois:',d1)





