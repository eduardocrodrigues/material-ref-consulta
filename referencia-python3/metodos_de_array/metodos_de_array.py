##################################
#
#    Metodos de array
#
##################################

print('-=' * 50)
print('--------- Metodos de Array ---------')
print('-=' * 50)
print()


print('Um array comum.')
alfabeto = ['a', 'b', 'c']
print(alfabeto)
print()

#----------------------------------------
#
# inserindo dados em um array
#
#----------------------------------------

#####################################################
# incrementando dados no array usando o operador +=
print('O mesmo array acima incrementando mais itens á lista com os operadores +=')
print("    OBS: cada caractere da string: 'defg' entrará como um item de cada vez no array")
alfabeto = ['a', 'b', 'c']
alfabeto += 'defg'
print(alfabeto)
print()


########################################################
# incrementando dados no array usando o metodo extend()
print('estende a lista com a string inserida no parametro do metodo extend() como ')
print(' cada caractere sendo um item da lista de forma individual. ')
alfabeto = ['a', 'b', 'c']
alfabeto.extend('hijkl')
print(alfabeto)
print()

print()
print('O metodo extend() é usado para inserir vários itens em uma lista extendendo-a')
print('  OBS: vc pode também inserir uma lista dentro de outra lista com o método: extend()')
array2 = ['edu', 'we', 'dri']
print(array2)
array2.extend(['alex', 'nego', 'ana', 'alexandre'])# NÃO FAÇA assim: print(cursos.extend()), senão dará erro, primeiro faça array.extend(), depois use o print(), dessa forma os dados funcionarão corretamente, e lembre-se de inserir os colchetes no parametro do extend([]) e inserir os dados dentro dos colchetes.
print('depois de usado o metodo extend(), o array ficará assim:')
print(array2)
print()


####################################################
# inserindo dados no array usando o metodo append()
print('adiciona um item á lista com o metodo append()')
nomes = ['Neri', 'Selvino', 'Romilda']
nomes.append('Eduardo')
print(nomes)
print()


####################################################
# inserindo dados no array usando o metodo insert()
print('insere uma string no array com o metodo insert() definindo o indice no')
print('primeiro parâmetro, e definindo a string a ser inserida, no segundo parâmetro')
nomes = ['Neri', 'Selvino', 'Romilda']
nomes.insert(1,'Weverton')
print(nomes)
print()



#----------------------------------------
#
# fatiando dados de um array
#
#----------------------------------------

print('fatia alguns dados do array, mantendo os dados fatiados na lista original')
nomes = ['adriano', 'weverton', 'erica', 'eduardo']
nomes_fatiados = nomes[1:3]
print(nomes_fatiados)
print()

print('Fatia os dados da: list_1 para a: list_2, fazendo com que as duas listas')
print('possua os mesmos dados, mas as listas são alocadas em espaço de memória')
print('diferentes no computador')
list_1 = [1]
list_2 = list_1[:] # Esta parte do código descrito como [:] é capaz de produzir uma lista completamente nova.
list_1[0] = 2
print(list_2)
print()


#----------------------------------------
#
# FATIAMENTO - usando números negativos no fatiamento
#
#----------------------------------------
print('Veja a sintaxe baixo:')
print('          my_list[start:end]')
print()
print('para entender: ')
print()
print(' START - é o index do primeiro elemento INCLUIDO NO FATIAMENTO ')
print(' END - é o index do primeiro elemento NÃO INCLUIDO NO FATIAMENTO ')
print()
print('É assim que os índices negativos funcionam com o slice:')
print()
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1] #
print(new_list) # a saída é: [8, 6, 4]
print()

print('Se o START especifica um elemento que se encontra mais longe do que o ')
print('descrito pelo END (do ponto de vista inicial da lista), o fatiamento (slice) estará vazio:')
print()
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list) # a saída é: [], pq o fatiamento inicial FOI DEFINIDO COM VALOR INICIAL NEGATIVO e O VALOR FINAL FOI DEFINIDO COM VALOR POSITIVO.
print()

print('Se o parametro: START do fatiamento especificar um valor negativo,')
print(' e o parametro: END for especificado com vazio, será feito ')
print('o FATIAMENTO DA POSIÇÃO NEGATIVA DO ELEMENTO da lista, ATÉ O FINAL DA LISTA')
print(' ')
my_list = [1, 2, 3, 4, 5]
new_list = my_list[-2: ] # o valor: -1 da lista, é o ULTIMO ITEM DA LISTA, o valor: -2 da lista, é o PENÚLTIMO ITEM DA LISTA, E ASSIM POR DIANTE...
print(new_list) # a saída será: [4, 5]
print()

print('Fatiamento que deleta todos os elementos de dentro da lista, mantendo a lista')
print()
my_list = [10, 8, 6, 4, 2]
del my_list[:] # deletas todos os dados dentro da lista, mantendo a lista vazia...
print(my_list)
print()
print('A remoção do slice no código muda dramaticamente o significado do código')
print('   OBS: a instrução: del, eliminará a lista em sí, e não somente o seu conteúdo')
my_list = [10, 8, 6, 4, 2]
del my_list # remove a lista, e não somente o conteudo dentro da lista !!!
#print(my_list) #gerará um erro, pq a lista foi excluida (não existe mais) !!!
print()


############################################
# sintaxe para fazer fatiamento (SLICE) de arrays
print('array[2:] - fatia o array a partir do indice 2 até o final da lista.')
print('array[:5] - fatia o array do começo dele até (mas não inclusive) o indice 5.')
print('array[::2] - fatia o array do inicio ao fim de 2 em 2 itens.')
print('array[::-1] - exibe os valores do array de trás pra frente.')





#----------------------------------------
#
# removendo dados de um array
#
#----------------------------------------

#################################################
# removendo dados do array usando o metodo pop()
print('retira o último elemento do array com o metodo pop()')
alfabeto = ['a', 'b', 'c', 'd', 'e']
alfabeto.pop()
print(alfabeto)
print('Obs: voce pode remover o item que quiser do array com o pop(), basta')
print('inserir o indice do item a ser removido do array como parametro do pop()')
alfabeto2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
alfabeto2.pop(1)
print(alfabeto2)
print()

######################################################################
# removendo dados do array usando a palavra reservada: del, do python
print('deleta um item de um array pelo indice com o comando del alfabeto[2]')
alfabeto = ['a', 'b', 'c', 'd', 'e']
del alfabeto[2]
print(alfabeto)
print()

######################################################################
# Usando o operador: in, com listas
print('O operador: in, verifica se um dado elemento (O ARGUMENTO DA ESQUERDA) está ')
print('atualmente armazenado dentro da lista (O ARGUMENTO DA DIREITA). Se o argumento ')
print('da esquerda estiver na lista, será retornado: TRUE ')
my_list = [0, 3, 12, 8, 2]
print(5 in my_list) # Retorna True
print()

print('O operador: not in, verifica se um dado elemento (O ARGUMENTO DA ESQUERDA) NÂO ESTÀ ')
print('atualmente armazenado dentro da lista (O ARGUMENTO DA DIREITA). Se o argumento ')
print('da esquerda NÂO ESTIVER na lista, será retornado: TRUE ')
my_list = [0, 3, 12, 8, 2]
print(5 not in my_list) # Retorna True
print()


###############################################
#
print('remove os indices definidos nos colchetes menos o último indice ')
print('após os dois pontos dentro dos colchetes')
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
del alfabeto[2:4]
print(alfabeto)
print()


####################################################
# removendo dados do array usando o metodo remove()
print('remove o item do array inserindo o item desejado a ser removido no ')
print('parametro do metodo remove()')
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
alfabeto.remove('b')
print(alfabeto)
print('')



#------------------------------------------------------
#
#    Fazendo cópia de array em python
#
#------------------------------------------------------

print('Fazendo a copia de uma lista em outra variável, mas MANTENDO O MESMO ENDEREÇO DE MEMÓRIA,')
print('ou seja, o que for alterado em uma lista, a mesma coisa será alterada na outra.')
lista1 = ['weverton', 'ana', 'erica', 'dri']
lista2 = lista1 # Faz a cópia da lista MANTENDO O MESMO ENDEREÇO DE MEMÓRIA da lista anterior.
lista2.remove('erica')
print(lista2)
print(lista1)
print()


print('Fazendo a copia de uma lista em outra variável, mas TENDO UM ENDEREÇO DE MEMÓRIA DIFERENTE da lista anterior.')
print('ou seja, o que for alterado em uma lista, a mesma coisa NÃO SERÁ ALTERADA na outra.')
lista1 = ['weverton', 'ana', 'erica', 'dri']
lista2 = lista1[:] # Faz a cópia da lista TENDO UM ENDEREÇO DE MEMÓRIA DIFERENTE da lista anterior.
lista2.remove('dri')
print(lista2)
print(lista1)
print()


print('Fazendo a copia de uma lista em outra variável, mas TENDO UM ENDEREÇO DE MEMÓRIA DIFERENTE da lista anterior.')
print('ou seja, o que for alterado em uma lista, a mesma coisa NÃO SERÁ ALTERADA na outra.')
lista1 = ['weverton', 'ana', 'erica', 'dri']
lista2 = lista1.copy() # Faz a cópia da lista TENDO UM ENDEREÇO DE MEMÓRIA DIFERENTE da lista anterior.
lista2.remove('dri')
print(lista2)
print(lista1)
print()



#----------------------------------------------------------
#
#    Fazendo contagem de caracteres de um array em python
#
#---------------------------------------------------------

########################################################################
# fazendo contagem de caracteres em um array usando o metodo count()
print('retorna quantas vezes o item inserido no parametro de cont() apareceu no array com o metodo count()')
cursos = ['python', 'java','android', 'python', 'java', 'python']
print(cursos)
print('O curso apareceu: ', cursos.count('python'), 'vezez no array')
print('O curso apareceu: ', cursos.count('java'), 'vezez no array')
print('O curso apareceu: ', cursos.count('html'), 'vezes no array') # Retorna 0 pq não tem nenhum item com esse nome no array.
print()



#----------------------------------------------------------
#
#    Invertendo todos os dados de um array em python
#
#---------------------------------------------------------

################################
# usando o metodo reverse()
print('')
cursos = ['python', 'java', 'android', 'delphi', 'html', 'clipper']
print(cursos)
cursos.reverse() # NÃO FAÇA assim: print(cursos.reverse()), senão dará erro, primeiro faça array.reverse(), depois use o print(), dessa forma os dados funcionarão corretamente.
print(cursos)
print()


#------------------------------------------------------------------
#
#    Descobrindo o indice de um dado dentro de um array em python
#
#------------------------------------------------------------------

#############################
# usando o metodo index()
print('retorna o número do indice do elemento no array iserido como parametro no metodo index()')
cursos = ['python', 'java', 'android', 'delphi', 'html', 'clipper']
print(cursos)
print('O indice do item da lista é:', cursos.index('clipper'))
print()



#--------------------------------------------------------------------------
#
#    Organizando os dados em ordem alfabética dentro de um array em python
#
#--------------------------------------------------------------------------

############################
# usando o metodo sort()
print('ordena os itens da lista em ordem alfabética com o metodo sort()')
listanomes = ['neri', 'lisiane', 'giulia', 'gustavo']
print(listanomes)
listanomes.sort()
print(listanomes)
print()



#-----------------------------------------------------
#
#    Removendo os dados dentro de um array em python
#
#-----------------------------------------------------

print()
print('o metodo clear() limpa/remove todos os itens do array deixando ')
print('um array vazio, ex:')
array1 = ['eduardo', 'weverton', 'alex']
print(array1)
array1.clear()# NÃO FAÇA assim: print(cursos.clear()), senão dará erro, primeiro faça array.clear(), depois use o print(), dessa forma os dados funcionarão corretamente.
print('array depois de usar o clear()')
print(array1)
print()



#-----------------------------------------------------
#
#    Desempacotamento de dados de um array em python
#
#-----------------------------------------------------

lista = [1, 2, 3]

a, b, c = lista
print(a)
print(b)
print(c)


print('Desempacotando os valores de uma lista e imprimindo na tela os valores desempacotados')
lista = [1, 2, 3, 4, 5]
print('valores desempacotados da lista: ', *lista)
print('  OBS: podemos imprimir na tela os valores de uma lista de forma DESEMPACOTADA COM O CARACTER (-) COMO SEPARADOR.')
print(*lista, sep='-')


print('desempacotando somente os valores que eu quiser')
lista = [1, 2, 3, 4, 5]

a, b, _, d, _ = lista

print(a)
print(b)
print(d)


print('desempacotando os primeiros valores de uma lista, e o restante dos valores mantendo na mesma lista')
lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista  # a variável *n é a variável que mantém o restante dos valores da lista, na lista.
print(n1, n2, n)



#--------------------------------------------------
#
#  imprimindo valores de uma tupla (tuplas é como um array,
#  só que seus dados são imutáveis, ou seja, seus dados
#  não podem ser alterados)
#
#--------------------------------------------------

print('para imprimir valores de uma tupla (lista imutável) que contém tipos de dados diferentes,')
print('utilize o loop for com range(), com o método len() dentro do segundo parâmetro do range(), ex:')

listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.90)
print(listagem)
print()
for i in range(0, len(listagem), 2):
    print('imprimindo um item sim, um item não, na listagem da tupla:')
    print(listagem[i])
    print('  OBS: Nesse caso, como a string aparece a cada dois itens do array em sequência,')
    print('utilizamos o terceito parâmetro no método: range() com valor 2, para que o loop pule a cada dois itens')
    print('do array (começando do indice 0, como definido no primeiro parametro do range(), onde')
    print('o indice 0 contêm a primeira string da tupla, e assim pegando cada string a cada dois indices')



print('Metodos estudados:')

print('clear()')
print('count()')
print('index()')
print('insert()')
print('pop()')
print('remove()')
print('sort()')
print('reverse()')
print('extend()')
print('append()')
print('copy()')


#######################################################
# link da documentação python para métodos de array:
#
# https://docs.python.org/pt-br/3/tutorial/datastructures.html
