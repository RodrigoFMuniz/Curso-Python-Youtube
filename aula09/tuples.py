t1 = (1,1,1,10,3,3,5,6,3) # Com um elemento é necessária a inserção da virgula
print('Tupla 1:',t1)
print('Tipo da tupla:',type(t1))
print(dir(t1))
print('Contador de itens 1 : ',t1.count(1))
print('Indice do item 10: ',t1.index(10))

print('Recuperando valores atômicos da tupla: ',t1[3])
# Se tentar inserir um novo valor em qq indice, ocorrerá um erro: TypeError: 'tuple' object does not support item assignment
t1[3] = 20
print('Tupla 1:',t1)