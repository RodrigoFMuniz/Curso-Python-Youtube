palavra_1 = 'Hello World'
ascii_1 = []

for l in palavra_1:
    print(f'{ord(l)} -> {l}')
    ascii_1.append(ord(l))


for b in ascii_1:
    print(f'{chr(b)}->{b}')