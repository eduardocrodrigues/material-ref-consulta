###########################################
#
#    Métodos de String 
#
###########################################

print('-*-'*5)
print('-----Metodos de String --------')
print('entenda os metodos usando o nome: eduardo chagas rodrigues')
print('-*-'*50)


nome = input('Digite seu nome: ')
print('Capitalize() = primeiro caractere é Maiúsculo, o restante da string fica tudo em minúsculo: ', nome.capitalize())
print()
print('Center() = centraliza dentro dos espaços em branco definidos: ', nome.center(30))
print()
print('count() = Conta quantas letras tem no nome ', nome.count('e'))
print()
print('endswith() = Retorna True se o nome terminar com a(s) letra(s) definidas no parametro: ', nome.endswith('rdo'))
print()
print('startswith() = Retorna True se o nome começar com a(s) letra(s) definidas no parametro: ', nome.startswith('edu'))
print()
print('find("d") = retorna a posição da string: ', nome.find('d'))
print()
print('find("d",2) = procura a substring (no caso, a substring "d") a partir da posição (2) da string :' ,nome.find('d', 2))
print()
print('find("r",3,5) = retorna a posição da string entre dois índices escolhidos: ', nome.find('r',3,5))
print('OBS: TANTO find() QUANTO index() PROCURAM UMA SUBSTRING EM UMA STRING A PARTIR DE UM DETERMINADO')
print('INDICE OU PROCURAM UMA SUBSTRING ENTRE DOIS INDICES (definidos no parâmetros do método) ')
print()
print('rindex() - faz o mesmo que o metodo "index()", só que começa a procura pelo')
print('indice da direita para a esquerda.', nome.rindex('a'))
print('Index() = retorna a posição da primeira ocorrêcia da substring: ', nome.index('d'))
print()
print('index() = retorna a posição da segunda ocorrêcia da substring: ', nome.index('d', 2))
print()
print('rindex() - faz o mesmo que o metodo "index()", só que começa a procura pela')
print('substring da direita para a esquerda.', nome.rindex('d'))
print('lower() = retorna as strings com letras minúsculas: ', nome.lower())
print()
print('upper() = retorna as strings com letras maiúsculas: ', nome.upper())
print()
print('title() = retorna com o primeiro caractere da primeira palavra da string em maiúsculo: ', nome.title())
print()
print('"-".join() = insere o item entre cada caractere da string ou entre cada item/indice de um array: ', '-'.join(nome))
print()
print('ljust() = justifica a string a esquerda: ', nome.ljust(30), 'casa')
print()
print('rjust() = justifica a string a esquerda: ', nome.rjust(30), 'casa')
print()
print('partition() = divide a string em uma tupla com tres elementos: ', nome.partition('ar'))
print()
print('rpartition() = divide a string em uma tupla')
print('com tres elementos ( dos elementos do lado direito da string): ', nome.rpartition('ar'))
print()
print('strip() = retira caracteres em branco á esquerda e a direita da string: ',"   eduardo    ".strip())
print()
print('lstrip() = retira caracteres em branco somente do lado esquerdo da string: ', "   eduardo   ".lstrip())
print()
print('rstrip() = retira caracteres em branco somente do lado direito da string: ', "   eduardo   ".rstrip())
print()
print('split() = divide uma string e retorna em uma lista: ', nome.split())
print('O padrao para divisao da string é o caractere em branco que separa as palavras')
print('na string, mas vc pode dividir a string a partir de um caractere de virgula (,)')
print('é so colocar o caractere de vírgula dentro dos parênteses do metodo split().')
print('  OBS: o caractere inserido como parametro no split() é removido.')
print('  OBS2: O método .split() pode ser usado para criar atribuições multiplas, exemplo:
print('   (ritmo, vocalista, vocais, baixista) = bandaRock.split() ')
print('  com o arquivo bandaRock acima, estamos usando atribuição multipla para variáveis')
print('  definidas dentro de parênteses para atribuir os valores das linhas divididas')
print('  com split() para as variáveis: ritmo, vocalista, vocais e baixista.')
print('  # o número de valores divididos no(s) arquivo(s) tem que ser equivalente ao')
print('  # mesmo número de váriáveis definidas na atribuição multipla.')
print()
print('rsplit() - faz o mesmo que "split()", só que começa a dividir a string da direita para a esquerda.')
print()
print('zfill() = preenche a esquerda da string com números zeros (0): ', '465'.zfill(8))
print()
print('swapcase() = inverte caracteres maiúsculos para minusculos e minúsculos para maiúsculos: ', "Eduardo Chagas")
print()
print('encode(x, y) - o primeiro parametro define o tipo de encode ("utf-8", ascii,etc...)')
print('e o segundo parametro define o tipo de resposta de erro, se caso der erro.')
print('''
############################################
#tipos de resposta de erros encode abaixo:
strict - resposta padrão que aumenta a exceção 'UnicodeDecodeError' em caso de falha.
ignore - ignora o unicode não codificado do resultado.
replace - substitui o unicode não codificado por um ponto de interrogação ?.
xmlcharrefreplace - Insere uma referência de caractere XML em vez de unicode não codificável.
backslashreplace - insere uma seqüência de espaço \uNNNN em vez de unicode não codificável.
namereplace - insere uma sequência de escape \ N {...} em vez de unicode não codificável.
''')
print()
print('casefold() - faz o mesmo que o metodo lower():', nome)
print()
print('expandtabs() - expande a tabulação definida com "\t", o padrao de tabulação é 8, mas')
print('você pode definir quantos espaços quiser inserindo um ')
print('número como parametro:', "eduardo\tchagas\trodrigues".expandtabs(4))
print()
nome1 = 'eduardo'
idade = 28
print('format() - usado para inserir valores formatados na string. ex: ')
print('o meu nome é {} e eu tenho {} anos.'.format(nome1, 28))
print()
dicionario = {'x':4,'y':-5, 'z': 0}
('format_map() - faz o mesmo que o ".format()", diferença é que ele é usado')
print('somente para exibir os valores do dicionario na string usando as chaves. ex:')
print("dicionario = {'x':4,'y':-5, 'z': 0}")
print('valores das chaves do dicionario: {x} {y} {z}'.format_map(dicionario))
print()
stringNome = 'eduardo\nchagas\nrodrigues\n1989'
stringNome2 = 'eduardo chagas rodrigues 1989' # use esta string no splitlines para ver a diferença.
print('splitlines() - divide a string onde encontra \n (quebra de linha) em substrings e retorna')
print('as strings em um array. ex:',stringNome.splitlines(True))
print('OBS: caso queira mostrar onde estão os \n, insira o valor booleano True no parametro.')
print()
string = 'amigos transparentes juntos'
palavra1 = 'aeuos'
palavra2 = '12345' #pode ser com caracteres tbm, so usamos números para facilitar a visualização.
naoUsados = 'es' #o numero da letra 's' é 115, e o numero da letra 'e' é 101.
print('maketrans(x, y, z) - retorna o número da letra (toda letra do teclado é representada por um número).')
print('caso insira dado somente no primeiro parametro, o metodo só aceitará um dicionario,')
print('caso insira 2 parametros, retornara um dicionario com o primeiro parametro como chave e o segundo')
print('parametro como valor (ambos com o numero que representa o caractere, ex: o numero da tecla "a" é 97,')
print('o numero da tecla "b" é 98, o número da tecla "c" é 99...), caso defina o metodo com 3 parametros, o')
print('o terceiro parametro define os caracteres que não serão usados.', string.maketrans(palavra1, palavra2, naoUsados))
print()
string1 = 'fazendo amigos e compartilhando conhecimento'
caracteres1 = 'aenro' # os caracteres dessa variavel
caracteres2 = '73925' # tem que ter o mesmo tamanho dessa 
caracteresRemovidos = 'er' # remove na troca dos caracteres
x = string1.maketrans(caracteres1, caracteres2, caracteresRemovidos) # variavel que vai no translate
print('translate() - faz a troca dos caracteres das strings definidas nos parametros')
print('do maketrans(), prepara os caracteres do primeiro parametro do')
print('metodo maketrans() para TROCAR pelos caracteres do segundo parametro do')
print('metodo maketrans().')
print('OBS:as strings do metodo maketrans() tem que ter O MESMO TAMANHO.', string1.translate(x)) 
print()



# metodos de string
'''
captalize()
center()
count()
startswith()
endswith()
find()
index()
upper()
lower()
title()
join() 
rjust()
ljust()
partition()
rpartition()
split()
strip()
lstrip()
rstrip()
zfill()
swapcase()
casefold()
encode(x, y)
expandtabs()
format()
format_map()
rindex()
rfind()
rsplit()
splitlines()
maketrans(x, y, z)
translate()
replace()

#########################################################################
# esses métodos abaixo está no arquivo: metodos_de_string_boleanos.py
isalpha()
isdecimal()
isdigit()
isnumeric()
islower()
isupper()
istitle()
isspace()
isalnum()
isascii()
isindentifier()
isprintable() 

'''
 















