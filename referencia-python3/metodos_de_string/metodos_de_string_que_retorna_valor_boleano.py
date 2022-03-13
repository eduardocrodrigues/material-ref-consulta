##################################################
#
# Métodos de string que retorna valor boleano
#
##################################################

print('-----Metodos de string com valores boleanos--------')
print('---- ou seja, retorna valor True ou False ----')


print('isalpha() = verifica se o valor é alfabetico: ', 'eduardo'.isalpha())
print()
print('Os três métodos abaixo são métodos diferentes, mas fazem a mesma coisa:')
print('isdecimal() = verifica se o valor dentro da string é decimal, ou seja, 10, 20, 30...: ', "3045".isdecimal())
print('isdigit() = verifica se o valor dentro da string é numero: ', "2974".isdigit())
print('isnumeric() = verifica se o valor é numérico: ', "7895".isnumeric())
print()
print('islower() = verifica se a string está toda em minúscula: ', "Eduardo".islower())
print()
print('isupper() = verifica se a string está toda em maiúscula: ', "EDUARDO".isupper())
print()
print('istitile() = verifica se a cada primeira letra de cada palavra está em maiúscula: ', "Estudo Sobre Python".istitle())
print()
print('isspace() = verifica se a variável é vazia: ')
print('exemplo1', "   \t".isspace()) # o caractere de tabulação é contado como espaço vazio...
print('exemplo2', "   ".isspace()) # e a string vazia é vazia, óbvio, rsrsrsrsr
print()
print('isalnum() = verifica se a string é alfanumérica (ou seja, verfica se na string contêm letras e numeros): ', "edu457ardo".isalnum())
print()
print('isidentifier() = verifica se o primeiro caractere (ou os primeiros caracteres) da string começa com qualquer caractere do')
print('alfabeto, seguido de caracteres de letras ou de números')
print('  OBS: Se no começo da string conter: número(s), ou qualquer tipo de caractere especial (ex: !, @, #, &, etc...), o valor retornado será: False')
print('  OBS2: Se em qualquer lugar da string conter o caractere vazio, o valor retornado será: False')
print('valor retornado: ', "edu3376".isidentifier())
print()
print('isprintable() = verifica se a string pode ser impressa no python')
print('exemplo1: ', "Space is a printable".isprintable())
print('  OBS: string com o caractere: "\n" dentro da string, não permite que a string seja impressa no python')
print('exemplo2: ', "\nNew Line is printable".isprintable())  
print()
print('verifica se a string pertence ao padrão de caracteres da tabela ASCII')
print('  OBS: a tabela ASCII é a tabela que representa o padrão de caracteres do alfabeto americano')
print('exemplo de código de string com caracteres americanos:')
print('exemplo1:', "welcome".isascii())
print('exemplo2:', 'welcome कखग'.isascii()) # veja que a string CONTÊM CARACTERES que NÂO PERTENCEM a tabela ASCII (a string contêm caractere árabe




