#Variáveis declaradas

a = "Hello World !!!"
b = 10
c = 10.0

#Impressão

print("Hello world diretamente no argumento da função")
print(a)
print('Texto', a)
print('Texto concatenado ' + a)
# print('Texto concatenado ' + b) # Não pode concatenar non srings com string. é necessário o parse antes.
print('Texto concatenado ' + str(b))

# Impressões formatadas

print("Texto formatado: %s" %a)
print("Texto formatado: %s e %d" %(a, b))
print("Texto formatado: %s e %f" %(a, c))

# Usando .format

print("Texto formatado: {}".format(a))
print("Texto formatado: {} e {}".format(a, b))
print("Texto formatado: {} e {:.3f}".format(a,c))

# f strings

print(f'{a} - {b} - {c:.2f}')
print(f'{a} - {b + 100} - {c:.2f}')
