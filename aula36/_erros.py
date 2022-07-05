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
    name = {'oi':'olá'}
    print(name['oi'])
except NameError as error:
    print(f'error do tipo NameError: {error}')
except ValueError as error:
    print(f'Erro do tipo ValueError: {error}')
except KeyError as error:
    print(f'Erro do tipo KeyError: {error}')
except IndexError as error:
    print(f'Erro do tipo IndexError: {error}')
else:
    print('Finalizado')
