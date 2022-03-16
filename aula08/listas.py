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

# Count

l1.append(2)
l1.append(2)
l1.append(3)
l1.append(3)
l1.append(3)
l1.append(3)
l1.append(4)
print('Lista 1 (after appends):', l1)
print('Qtd de valores 3 na lista ==',l1.count(3))

