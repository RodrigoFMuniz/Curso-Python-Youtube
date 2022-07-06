def sum(n1,n2):
    try:
        return n1+n2
    except Exception as e:
        print('Erro: ',e) #modifica o comportamento da linguagem python
        raise TypeError('Os valores devem se numéricos')

try:
    sum(1,'w')
except TypeError as e:
    print(e)