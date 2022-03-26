# If

a = 3

if a == 3:
    print('Deu match!!!')

# else

b = 'Superman'

if b == 'Batman':
    print('É o batman')
else:
    print(f'Não é o batman. É o {b}.')

# Elif

c = bin(12)

if c =='0b1001':
    print('Retornou 9 em binário')
elif c == '0b1100':
    print('Retornou 12 em binário')
elif c == '0b1000':
    print('Retornou 8 em binário')
elif c == '0b1010':
    print('Retornou 10 em binário')
else:
    print(f'Outro número {c}')
