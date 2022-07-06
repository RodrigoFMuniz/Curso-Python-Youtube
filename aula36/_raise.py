def sum(n1,n2):
    try:
        return n1+n2
    except Exception as e:
        print('Erro: ',e)

sum(1,'w')