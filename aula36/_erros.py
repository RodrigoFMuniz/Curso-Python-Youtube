'''
NameError: A variável não foi definida
TypeError: Tipos de dados incompatíveis
RuntimeError: Erro de execução
SyntaxError: A sintaxe digitada é inválida e não reconhecida pelo compilador
ZeroDivisionError: Divisão por zero
IndexError: Índice está fora da correção
ValueError: Erro de valor inserido
'''

# NameError

try:
    name = 'Rodrigo'
    print(int(name))
except NameError as error:
    print(f'error: {error}')
except ValueError as error:
    print(f'Erro: {error}')
else:
    print('Finalizado')
