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
print('Dict 1 (get) Depois:',d1)



