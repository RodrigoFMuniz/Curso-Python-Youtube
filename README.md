# Curso Python - Básico ao intermediário Youtube

## Roadmap

![Rodamap](readme.assets/roteiro_de_aula.png)

## Aula 1

### Declaração de variáveis

    a = 'Hello World !!!'
    b = "Nova declaração"

    print(a)
    print(b)

    b = a

    print(b)

## Aula 02

### Comentários

    # Comentário de uma linha

    a = 'Hello World !!!' # comentário de uma linha em sequência ao script
    b = "Nova declaração"

    '''
    Comentário de múltiplas
    linhas
    '''

    c = '''
    Comentário de múltiplas
    linhas atribuído a uma variável
    '''
    d = # Gerará um erro

    print(a)
    print(b)
    print(c)
    print(d)

## Aula 03

### Strings

    #Variáveis declaradas

    a = "Hello World !!!"
    b = 10
    c = 10.0

    #Impressão

    print("Hello world diretamente no argumento da função")
    print(a)
    print('Texto', a)
    print('Texto concatenado ' + a)
    # print('Texto concatenado ' + b) # Não pode concatenar non srings com string. é necessário o parse antes.
    print('Texto concatenado ' + str(b))

    # Impressões formatadas

    print("Texto formatado: %s" %a)
    print("Texto formatado: %s e %d" %(a, b))
    print("Texto formatado: %s e %f" %(a, c))

    # Usando .format

    print("Texto formatado: {}".format(a))
    print("Texto formatado: {} e {}".format(a, b))
    print("Texto formatado: {} e {}".format(a,b))

    # f strings

    print(f'{a} - {b} - {c:.2f}')
    print(f'{a} - {b + 100} - {c:.2f}')
