l1 = [1]

print('Lista 1:',l1)
print(type(l1))

# Métodos disponíveis
print(dir(l1))

# Append
result_after_append = l1.append(2)
print('lista 1 (append):', l1)
print('res_append: ',result_after_append)

# Insert
result_after_insert = l1.insert(0,'entrou antes do valor que estava no index 0')
print('lista 1 (insert):', l1)
l1.insert(2,'entrou depois do valor que estava no index 1')
print('lista 1 (insert):', l1)
print('res_insert: ',result_after_insert)

# Pop
result_after_pop = l1.pop()
print('Lista 1 (Pop):', l1)
print('res_pop: ',result_after_pop)
result_after_pop_2 = l1.pop(0)
print('Lista 1 (Pop):', l1)
print('res_pop: ',result_after_pop_2)

# 


