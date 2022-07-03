'''
NameError: A variável não foi definida
TypeError: Tipos de dados incompatíveis
RuntimeError: Erro de execução
SyntaxError: A sintaxe digitada é inválida e não reconhecida pelo compilador
ZeroDivisionError: Divisão por zero
IndexError: Índice está fora da correção
'''

# NameError

try:
    print(name)
except NameError:
    print(NameError)
else:
    print('Finalizado')
