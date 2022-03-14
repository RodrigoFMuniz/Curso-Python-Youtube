''' 

TIPOS

O tipo é uma forma de classificar as informação. As linguagens de programação normalmente trazem implementado o que é chamado de tipos primitivos, isto é, o tipo de dado mais genérico possível.

Toda informação que manipularemos será, por definição, de um tipo.


TIPOS PRIMITIVOS

Tipo Primitivo são os tipos de dados mais simples, isto é, a informação em sua forma mais primitiva. Bons exemplos de valores primitivos são os caractere, os número, o valor True e o False e etc. A documentação do Python não trata os tipos de dados elementares (primitivos) com a nomenclatura normalmente encontrada na documentação da maioria das linguagens: Tipo Primitivo. Na documentação oficial, os tipos primitivos são chamados de tipos built-ins ou então, tipos construídos. Essa nomenclatura é utilizada para indicar que estamos utilizando informações que foram definidas, por padrão, através de classes dentro da Máquina Virtual do Python.

Nesse momento, chamaremos de Tipos Primitivos as informações em sua forma mais simples, porém, é importante saber que para o Python, não há tipo primitivos, mas sim, estruturas de dados que estão definidas, na maior parte das vezes, dentro da própria Máquina Virtual do Python.

É normal que as linguagens de programação tenham um conjunto de tipos chamados de: tipos primitivos. Devemos pensar nessa classificação como sendo os tipos primários de informações, como por exemplo, o tipo numérico. Como sabemos, todo número é constituído por algarismos. Dessa forma, o tipo numérico pode ser qualquer valor que seja composto por 1 ou mais caracteres numéricos.

Dessa forma, isto é, tendo a certeza de que uma variável declarada como sendo do tipo numérico inteiro sempre terá um valor numérico válido, somos capazes de desenvolver funções especificas que manipulam esse tipo de dado de maneira muito mais eficiente e sem a necessidade de verificação se o tipo da informação contida em determinada variável é válido.

Da mesma forma, temos o tipo de dado que representa conjuntos de caracteres, que na programação, é comumente chamado de String e o Python o chama de str. As String são capazes de armazenar conjuntos de caracteres que estão dispostos numa determinada ordem. Todas as vezes que estivermos manipulando dados que contenha caracteres - o tipo mais primitivo, isto é, a maneira mais abstrata para representarmos caracteres - estaremos utilizando uma variável definida como sendo do tipo str.

O fato de o Python não trabalhar com tipo primitivos diretamente, deve-se ao fato de que em Python, tudo são objetos. Dessa forma, o que chamaríamos de primitivo é, em Python, representado como uma e toda informação será, um objeto propriamente dito. A seguir, temos a lista dos principais tipos built-ins da linguagem Python:

int - para números inteiros
str - para conjunto de caracteres
bool - armazena True ou False
list - para agrupar um conjunto de elementos
tupla - semelhante ao tipo list, porém, imutável
dic - para agrupar elementos que serão recuperados por uma chave

O Python fornece um conjunto de tipos básicos bastante amplo e que normalmente, atendem a maioria das necessidades. Cada tipo citado, possui um conjunto de funções e métodos que permitem manipularmos as informações, contidas na variável, de maneira bastante eficiente.

Sempre que formos criar um novo tipo de dados, acabaremos utilizando os tipos básicos da linguagem, como por exemplo, o tipo `int`, ou então, o tipo `str` e assim por diante.



DIFERENÇA ENTRE TIPO E VALOR

O valor é qualquer informação, seja um número, texto, música, vídeo e etc. O tipo por sua vez, é a estrutura da informação e a forma de classificarmos os dados.

Todo valor numérico deve ser capaz de ser somado a outro valor, ou então, subtraido. Da mesma forma que todo texto, deve ser capaz de ser concatenado a outro, isto é, ser juntado a outro conjunto de caracteres.

O tipo da informação deve ser pensado como uma forma de classificarmos as diferentes informações e assim, termos a disposição um conjunto de funções para tratarmos e modificarmos os valores.

É importante saber que somos capazes de criar novos tipos de dados a qualquer momento, e a programação orientada a objetos é, em sua definição mais primitiva, uma maneira de criarmos novos tipos abstratos e definirmos, na estrutura da classe, funções, métodos, verificações que busquem tratar valores que tenham uma mesma estrutura.

Em Python tudo é tratado como objeto

Existem 4 tipos para classificação para os tipos de informações.

Tipos simples - constituidos por simples blocos, como int() e float()
Tipos de contêiner - objetos capazes de conter outros objetos
Tipos de código - objetos encapsuladores de elementos dos nosso programas
Tipos internos - tipos que serão utilizados durante a execução do nosso programa

'''