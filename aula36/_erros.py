'''
NameError: A variável não foi definida
TypeError: Tipos de dados incompatíveis
RuntimeError: Erro de execução
SyntaxError: A sintaxe digitada é inválida e não reconhecida pelo compilador
ZeroDivisionError: Divisão por zero
IndexError: Índice está fora da correção
ValueError: Erro de valor inserido
'''

try:
    # name = {'oi':'olá'}
    x = 1/1
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
    print('Usado o else')
finally:
    print('Finalizado')
