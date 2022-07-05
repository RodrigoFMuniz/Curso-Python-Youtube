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

from decimal import DivisionByZero


try:
    # name = {'oi':'olá'}
    x = 1/0
    print(x)
except NameError as error:
    print(f'error do tipo NameError: {error}')
except ValueError as error:
    print(f'Erro do tipo ValueError: {error}')
except KeyError as error:
    print(f'Erro do tipo KeyError: {error}')
except IndexError as error:
    print(f'Erro do tipo IndexError: {error}')
except ZeroDivisionError as error:
    print(f'Erro do tipo ZeroDivisionError: {error}')
else:
    print('Finalizado')
