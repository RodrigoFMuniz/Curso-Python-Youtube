s1 = {1,2,3,4,4,5,6} # valores repetidos são ignorados

print('Set 1: ', s1)
print('Tipo: ', type(s1))
print('Métodos ', dir(s1))

# Add, Não retorna valor

print(s1.add(7))
print('Set 1 após add: ',s1)

#Pop

print('Printando o retorno após o pop: ',s1.pop())
print('Set 1 após pop: ',s1)
print('Printando o retorno após o pop: ',s1.pop()) #Retira o primeiro item do set
print('Set 1 após pop: ',s1)