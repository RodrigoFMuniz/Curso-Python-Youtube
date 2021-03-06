s1 = {1,2,3,4,4,5,6} # valores repetidos são ignorados

print('Set 1: ', s1)
print('Tipo: ', type(s1))
print('Métodos ', dir(s1))

# Add, Não retorna valor

print(s1.add(7))
print('Set 1 após add: ',s1)

#Pop - retorna o valor o removido

print('Printando o retorno após o pop: ',s1.pop())
print('Set 1 após pop: ',s1)
print('Printando o retorno após o pop: ',s1.pop()) #Retira o primeiro item do set
print('Set 1 após pop: ',s1)

# Remove

print('Printando o retorno após o remove: ',s1.remove(4))
print('Set 1 após remove: ',s1)

# Update

s2 = {10, 20, 30, 40, 50, 60, 200}
print('Set 1 antes do update: ',s1)
print('Set 2 antes do update: ',s2)

print('Retorno após o update de s1 com s2: ', s1.update(s2))

print('Set 1 após do update: ',s1) #s1 alterado permanentemente
print('Set 2 após do update: ',s2)

# Union - Não altera os sets

s3 = {100,200,300,400}
print('Set 1 antes do union: ',s1)
print('Set 3 antes do union: ',s3)
print('Resultado do union: ',s1.union(s3))
print('Set 1 após do union: ',s1)
print('Set 3 após do union: ',s3)

# Difference - Um conjunto - outro conjunto - Não altera nenhum dos sets envolvidos

print("S1 - S3: ",s1.difference(s3))
print("S3 - S1: ",s3.difference(s1))
print('Set 1 após difference: ',s1)
print('Set 3 após difference: ',s3)

# Interesection - Não altera nenhum dos sets envolvidos

print("S1 and S3: ",s1.intersection(s3))
print("S3 and S1: ",s3.intersection(s1))
print('Set 1 após intersection: ',s1)
print('Set 3 após intersection: ',s3)

# Difference_update - altera os sets envolvidos 

print('Set 1 antes de difference: ',s1)
print('Set 3 antes de difference: ',s3)
print("S1 - S3: ",s1.difference_update(s3))
print('Set 1 após difference_update: ',s1)
print('Set 3 após difference_update: ',s3)

#Intersection_Update - altera os sets envolvidos permanentemente

s4 = {5,6,40, 1000, 2000}
print('Set 1 antes de intersection: ',s1)
print('Set 4 antes de intersection: ',s4)
print("S1 and S3: ",s1.intersection_update(s4))
print('Set 1 após intersection: ',s1)
print('Set 4 após intersection: ',s4)

# Symetric_difference - Remove valores que existem simultaneamente nos dois conjuntos e retorna o restante

s5 = {2,3,5,40,200,100,1000}
print('Set 1 antes de symmetric_difference: ',s1)
print('Set 5 antes de symmetric_difference: ',s5)
print("S1 - S3: ",s1.symmetric_difference(s5))
print('Set 1 após symmetric_difference: ',s1)
print('Set 5 após symmetric_difference: ',s5)

# Symetric_difference_update - Atualiza permanentemente, não retorna valor algum

print('Set 1 antes de symmetric_difference_update: ',s1)
print('Set 5 antes de symmetric_difference_update: ',s5)
print("S1 - S3: ",s1.symmetric_difference_update(s5))
print('Set 1 após symmetric_difference_update: ',s1)
print('Set 5 após symmetric_difference_update: ',s5)


# Discard - Elimina um item do set, não retorna valores. Semelhante ao remove

print('Set 1 (Discard):',s1)
print(s1.discard(100))
print('Set 1 (Discard):',s1)

# Copy
print('Set 1 (Copy):',s1)
s6 = s1.copy()
print('Set 6 (Copy):',s6)
print('Id s1: ',id(s1))
print('Id s6: ',id(s6))

# Clear, remove todos os elementos do set, não retorna nada
print('Set 1 (Clear):',s1)
print('Clear s1: ', s1.clear())
print('Set 1 (Clear):',s1)




