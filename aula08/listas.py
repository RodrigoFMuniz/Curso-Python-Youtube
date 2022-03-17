l1 = [1]

print('Lista 1:',l1)
print(type(l1))

# Métodos disponíveis
print(dir(l1))

# Append - não retorna o valor removido
result_after_append = l1.append(2)
print('lista 1 (append):', l1)
print('res_append: ',result_after_append)

# Insert - não retorna o valor removido
result_after_insert = l1.insert(0,'entrou antes do valor que estava no index 0')
print('lista 1 (insert):', l1)
l1.insert(2,'entrou depois do valor que estava no index 1')
print('lista 1 (insert):', l1)
print('res_insert: ',result_after_insert)

# Pop - retorna o valor removido
result_after_pop = l1.pop()
print('Lista 1 (Pop):', l1)
print('res_pop: ',result_after_pop)
result_after_pop_2 = l1.pop(0)
print('Lista 1 (Pop):', l1)
print('res_pop: ',result_after_pop_2)

# Remove - não retorna o valor removido
result_after_remove = l1.remove('entrou depois do valor que estava no index 1')
print('Lista 1 (remove):', l1)
print('res_remove: ',result_after_remove)

# Count - retorna a quantidade do valor argumentado

l1.append(2)
l1.append(2)
l1.append(3)
l1.append(3)
l1.append(3)
l1.append(3)
l1.append(5)
l1.append(4)
print('Lista 1 (after appends):', l1)
print('Qtd de valores 3 na lista ==',l1.count(3))

# Index - retorna o indice do valor argumentado

print('Indice do item 4 ==', l1.index(4))
print('Indice do item 5 ==',l1.index(5))

# Reverse - não retorna valor. Inverte a lista

print('Reversed l1:', l1.reverse())
print('lista 1',l1)
print('Reversed l1 again:', l1.reverse())
print('lista 1',l1)

# Sort - não retorna valor. ordena a lista
print('lista 1 (Sort)',l1)
print('Sort l1 (Sort): ', l1.sort())
print('lista 1 (Sort)',l1)

# Sorted - retorna a lista ordenada, porém não a ordena permanetemente

print('lista 1: ',l1)
l1.append(4)
l1.append(3)
l1.append(1)
print('lista 1: ',l1)
print('lista 1(sorted): ',sorted(l1))
print('lista 1 after sorted: ',l1)

# Copy - Faz uma cópia independente da lista

l2 = l1.copy()

print('Lista 1(copy):',l1)
print('Lista 2 (copy):',l2)
print(l1 == l2)
print(id(l1) == id(l2))
l1.append('item teste')
print('Lista 1(copy):',l1)
print('Lista 2 after append(copy):',l2)

# Extend - Insere os valores da lista extendida. Não possui retorno
l3 = ['batata','feijão','arroz']
print('Lista 1 (extend)',l1.extend(l3))
print('Lista 1 (extend)',l1)

# Clear
print('Lista 1 before clear(clear):',l1)
print('Res l1 after clear: ',l1.clear())
print('Lista 1 before after(clear):',l1)



