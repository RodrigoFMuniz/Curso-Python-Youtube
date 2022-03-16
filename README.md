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

## Um pouco sobre como o Python trata as variáveis internas

### TIPOS PRIMITIVOS

**_Tipo Primitivo_** são os tipos de dados mais simples, isto é, a informação em sua forma mais primitiva. Bons exemplos de valores primitivos são os caractere, os número, o valor True e o False e etc. A documentação do Python não trata os tipos de dados elementares (primitivos) com a nomenclatura normalmente encontrada na documentação da maioria das linguagens: Tipo Primitivo. Na documentação oficial, os tipos primitivos são chamados de tipos **_built-ins_** ou então, **_tipos construídos_**. Essa nomenclatura é utilizada para indicar que estamos utilizando informações que foram definidas, por padrão, através de classes dentro da Máquina Virtual do Python.

Nesse momento, chamaremos de Tipos Primitivos as informações em sua forma mais simples, porém, é importante saber que para o Python, **não há tipo primitivos**, mas sim, estruturas de dados que estão definidas, na maior parte das vezes, dentro da própria Máquina Virtual do Python.

É normal que as linguagens de programação tenham um conjunto de tipos chamados de: tipos primitivos. Devemos pensar nessa classificação como sendo os tipos primários de informações, como por exemplo, o tipo numérico. Como sabemos, todo número é constituído por algarismos. Dessa forma, o tipo numérico pode ser qualquer valor que seja composto por 1 ou mais caracteres numéricos.

Dessa forma, isto é, tendo a certeza de que uma variável declarada como sendo do tipo numérico inteiro sempre terá um valor numérico válido, somos capazes de desenvolver funções especificas que manipulam esse tipo de dado de maneira muito mais eficiente e sem a necessidade de verificação se o tipo da informação contida em determinada variável é válido.

Da mesma forma, temos o tipo de dado que representa conjuntos de caracteres, que na programação, é comumente chamado de String e o Python o chama de str. As String são capazes de armazenar conjuntos de caracteres que estão dispostos numa determinada ordem. Todas as vezes que estivermos manipulando dados que contenha caracteres - o tipo mais primitivo, isto é, a maneira mais abstrata para representarmos caracteres - estaremos utilizando uma variável definida como sendo do tipo str.

O fato de o Python não trabalhar com tipo primitivos diretamente, deve-se ao fato de que em Python, tudo são objetos. Dessa forma, o que chamaríamos de primitivo é, em Python, representado como uma e toda informação será, um objeto propriamente dito. A seguir, temos a lista dos principais tipos built-ins da linguagem Python:

- int - para números inteiros
- str - para conjunto de caracteres
- bool - armazena True ou False
- list - para agrupar um conjunto de elementos
- tupla - semelhante ao tipo list, porém, imutável
- dic - para agrupar elementos que serão recuperados por uma chave

O Python fornece um conjunto de tipos básicos bastante amplo e que normalmente, atendem a maioria das necessidades. Cada tipo citado, possui um conjunto de funções e métodos que permitem manipularmos as informações, contidas na variável, de maneira bastante eficiente.

Sempre que formos criar um novo tipo de dados, acabaremos utilizando os tipos básicos da linguagem, como por exemplo, o tipo `int`, ou então, o tipo `str` e assim por diante.

DIFERENÇA ENTRE TIPO E VALOR

O valor é qualquer informação, seja um número, texto, música, vídeo e etc. O tipo por sua vez, é a estrutura da informação e a forma de classificarmos os dados.

Todo valor numérico deve ser capaz de ser somado a outro valor, ou então, subtraido. Da mesma forma que todo texto, deve ser capaz de ser concatenado a outro, isto é, ser juntado a outro conjunto de caracteres.

O tipo da informação deve ser pensado como uma forma de classificarmos as diferentes informações e assim, termos a disposição um conjunto de funções para tratarmos e modificarmos os valores.

É importante saber que somos capazes de criar novos tipos de dados a qualquer momento, e a programação orientada a objetos é, em sua definição mais primitiva, uma maneira de criarmos novos tipos abstratos e definirmos, na estrutura da classe, funções, métodos, verificações que busquem tratar valores que tenham uma mesma estrutura.

Em Python tudo é tratado como objeto

Existem 4 tipos para classificação para os tipos de informações.

- Tipos simples - constituidos por simples blocos, como int() e float()
- Tipos de contêiner - objetos capazes de conter outros objetos
- Tipos de código - objetos encapsuladores de elementos dos nosso programas
- Tipos internos - tipos que serão utilizados durante a execução do nosso programa

## Tipos

    # string

    string_1 = 'Esta é uma string'

    #integers

    int_1 = 10
    print(int_1)
    print(type(int_1))

    #floats

    float_1 = 10.00
    print(float_1)
    print(type(float_1))

    #Boolean

    bool_1 = True
    print(bool_1)
    print(type(bool_1))

    #tuple

    tuple_1 = (1,)
    print(tuple_1)
    print(type(tuple_1))

    #list

    lista_1 = [1,2,3,4,5,'item 1', False, [1,2,3]]
    print(lista_1)
    print(type(lista_1))

    #Dict

    dic_1 = {'item_1':'valor 1','item_2':10, 'item_3':10.00, 'item_4':True, 'item_5':{'item_aninhado_1':'valor aninhado 1'}}
    print(dic_1)
    print(type(dic_1))

    #set

    set_1 = {1,2,3,True,False,'valor',(1,2)}
    print(set_1)
    print(type(set_1))

    ### Resultados


    10
    <class 'int'>
    10.0
    <class 'float'>
    True
    <class 'bool'>
    (1,)
    <class 'tuple'>
    [1, 2, 3, 4, 5, 'item 1', False, [1, 2, 3]]
    <class 'list'>
    {'item_1': 'valor 1', 'item_2': 10, 'item_3': 10.0, 'item_4': True, 'item_5': {'item_aninhado_1': 'valor aninhado 1'}}
    <class 'dict'>
    {False, 1, 2, 3, (1, 2), 'valor'}
    <class 'set'>

## Strings

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

## Numbers, int and float

    n1 = 10
    n2 = 20.10

    #int

    print(n1.bit_count())
    print(n1.bit_length())
    print(n1.conjugate())
    print(n1.as_integer_ratio())

    # Float

    print(n2.fromhex('10.00'))
    print(n2.__add__(20))
    print(n2.__abs__())
    print(n2.__ceil__())
    print(n2.__floor__())
    print(n2.__lt__(10))
    print(n2.__gt__(10))
    print(n1.__bool__())
    print(n1.__format__('.2f'))
    print(n1.__dir__())
    print(n1.__hash__())

## Boolean

    b1 = False
    b2 = True

    print(type(b1))
    print(type(b2))

    print(b1)
    print(b2)

    print(b1.bit_count())
    print(b2.bit_count())

    print(str(b1))
    print(str(b2))

    b12s1 = str(b1)
    b22s2 = str(b2)

    print(type(b12s1))
    print(type(b22s2))

    print(b12s1.upper())
    print(b22s2.lower())
