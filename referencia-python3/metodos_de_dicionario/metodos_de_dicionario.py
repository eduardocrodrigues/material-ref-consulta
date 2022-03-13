print()
print('-'*5+'Entendendo Dicionário'+'-'*5 )
print()

print('exemplo de lista para comparar a diferença com dicionário')
listaNomes = ['Neri', 'Selvino', 'Romilda']
print(listaNomes)
print('para saber o primeiro indice da lista, use o comando abaixo...')
print('listaNomes[1]')
print('que retornando o valor abaixo...')
print(listaNomes[1])
print()

print('Estrutura de montagem de um Dicionário')
dicionarioNomes = { 1: 'Lisiane',
		    2: 'Giulia',
		    3: 'Gustavo' }

print(dicionarioNomes)
print()
print('No dicionário, os itens são acessados pela chave, e é a chave que')
print('retorna o valor do item do dicionário.')
print("Como no exemplo abaixo, dicionarioNomes[2] retorna o nome 'Giulia'. ")
print()
print(dicionarioNomes[2])
print()

print('Exempo abaixo retorna as chaves do dicionário')
print('dicionarioNomes.keys()')
print('o comando acima retorna as chaves do dicionario (mostradas na linha abaixo...)')
print(dicionarioNomes.keys())
print()

print('Exemplo abaixo retorna os valores atribuidos as chaves do dicionário.')
print('dicionarioNomes.values()')
print('o comando acima retorna os valores das chaves do dicionario')
print(dicionarioNomes.values())
print()

print('Outro exemplo de dicionário...')
dicionarioCursos = { 'Python': 130,
		     'Java': 110,
		     'Arduino':90 }

print(dicionarioCursos)
print()

print('No dicionário, os itens são acessados pela chave, e é a chave que')
print('retorna o valor do item do dicionário.')
print('Outro exemplo de como acessar os valores com as chaves nos dicionários.')
print("dicionarioCursos['Python']")
print('valor retornado...')
print(dicionarioCursos['Python'])
print()

#print('O preço do curso de Java é {}. '.format(dicionarioCursos['Java']))
print()

print('Para adicionar itens a um dicionario, faça como no exemplo abaixo...')
print("dicionarioCursos['Android'] = 146")
dicionarioCursos['Android'] = 146
print(dicionarioCursos)
print()


print('O dicionario com o metodo keys() retorna somente as chaves do dicionario')
print('ex: dicionarioCursos.keys() retorna os valores abaixo...')
print('DicionarioCursos: ',dicionarioCursos.keys())
print()

print('O dicionario com o metodo values() retorna somente os valores do dicionario')
print('ex: dicionarioCursos.values() retorna os valores abaixo...')
print('DicionarioCursos: ',dicionarioCursos.values())
print()

print('O dicionario com o metodo items() retorna as chaves e os valores do dicionario')
print('ex: dicionarioCursos.items() retorna os valores abaixo...')
print('DicionarioCursos: ',dicionarioCursos.items())
print()

print('Outra forma de usar o dicionario com o metodo: items(), é usando um loop for,')
print('que retorna as chaves e os valores do dicionario')
print('ex: dicionarioCursos.items() com o loop: for, retorna os valores abaixo...')
for keys, values in dicionarioCursos.items():
    print('DicionarioCursos: key ', keys, "-> values", values)
print()



print('*=-' * 10 +' Dicionário Com listas Como Valores ' + '-=*' * 10)

dicionarioCursos = { 'python': [ 130, 'basico', 'desktop' ],
		     'java': [ 110, 'intermediário', 'desktop' ],
		     'arduino': [ 90, 'avançado', 'robótica']     }

print(dicionarioCursos)
print()

print('for chave, informacoes in dicionarioCursos.items():')
print('Na variável chave é atribuida a chave do dicionário, e ')
print('na variável informacoes será atribuido o array de valores do dicionário...')
print('Você pode acessar o indice dos valores do dicionário da mesma forma como em uma lista comum.')
print('ex: informacoes[0], informacoes[1], e assim por diante...')
for chave, informacoes in dicionarioCursos.items():
    print('Curso: ', chave)
    print('Valor: R${:5.2f}'.format(informacoes[0]))
    print('Nivel: ', informacoes[1])
    print('Observação: ', informacoes[2])
print()


dicionarioCursos = { 'python': [ 130, 'basico', 'desktop' ],
		     'java': [ 110, 'intermediário', 'desktop' ],
		     'arduino': [ 90, 'avançado', 'robótica']     }

print()
print(dicionarioCursos)

print('exibe o valor da chave do dicionário... caso não exista')
print('a chave, retorna None (ou seja, não encontrado)')
print('Dados de Java (usando get()): ', dicionarioCursos.get('java'))
print()

print('O metodo fromkeys() com o dicionario gera um dicionario somente')
print('com chaves e com valores None..')
print('Obs: tem que colocar "[]" dentro dos parenteses do metodo para criar as chaves.')
print("d = dict1.fromkeys(['java', 'python', 'android'])")
dic1 = {}
d = dic1.fromkeys(['java', 'python', 'android'])
print(d)
print()

print('O metodo update() adiciona valores as chaves dos dicionários')
print('d.update(java=129)) #repare que a chave é inserida sem as aspas neste metodo.')
d.update(java=129)
print(d)
print()

print('Remove um item do dicionario (chave e valor) inserindo a chave do item')
print('a ser deletado (entre aspas) como parametro dentro do metodo pop()')
d.pop('android')
print(d)
print()

print('Remove o último item do dicionário (chave e valor)')
dictionary = {"flower": "flor", "bag": "mochila", "door": "porta"}
print(dictionary)
print()

dictionary.popitem()
print(dictionary)
print()

print('O método: copy() é usado para copiar todo um dicionário')
pol_eng_dictionary = {
    "zamek": "castle",
    "woda": "water",
    "gleba": "soil"
    }
print(pol_eng_dictionary)

copy_dictionary = pol_eng_dictionary.copy()
print('dicionario copiado para uma outra variável chamada: copy_dictionary...')
print('copy_dictionary: ', copy_dictionary)
print()



'''
outra forma de exibir chave e valor de um dicionario sem a função items(), ex:

roupas = {'camisa': 'echo', 'bermuda': 'rip_curl', 'blusa': 'oakley', 'cueca': 'lupo'}

print(roupas)
print()

for item in roupas:
    print(item, roupas[item])
'''


# Metodos de dicionários

'''

.keys() - retorna/exibe somente as chaves do dicionario.
.values() - retorna/exibe somente os valores das chaves do dicionario.
.items() - retorna/exibe as chaves e os valores do dicionario.
.clear() - limpa o dicionario removendo tudo, deixando o dicionario vazio.
.pop()  - Remove um item do dicionario (remove chave e valor) inserindo a chave do item a ser deletado (entre aspas) como parametro dentro do metodo pop().
.popitem() - remove um item qualquer, do dicionario
.get() - pega o valor do dado no dicionário e exibe, é só inserir a chave do dicionário como parametro dentro do get().
.update()  - adiciona valores as chaves dos dicionários (repare que a chave é inserida sem as aspas neste metodo).
.fromkeys() - gera um dicionario somente com chaves e sem valores.
.copy() - usado para copiar todo um dicionário. 
'''



