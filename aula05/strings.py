s1 = '    hello world !!!    '
s2 = 'Hello again ...'

print(s1.capitalize())
print(s1.title())
print(s2.lower())
print('Strip',s2.strip())
print('rstrip',s2.rstrip())
print('lstrip',s2.lstrip())
print('ljust',s2.ljust(3))
print('rstrip',s2.rjust(3))
print('Replace',s2.replace('l','*'))
print('Remove Suffix',s2.removesuffix('...'))
print('Remove Prefix',s2.removeprefix('Hel'))
print(s2.upper())
print("Number of 'a'", '=', s2.count('a'))
print("Number of 'l'", '=', s2.count('l'))
print("Number of ' '", '=', s2.count(' '))
print(s2.encode())
print(s2.endswith('.'))
print(s2.startswith('Hel'))
print('Position','=',s2.find('a'))
print('Is digit = ',s2.isdigit())
print('Index = ',s2.index('o'))
print(s2.isprintable())
print(s2.isnumeric())