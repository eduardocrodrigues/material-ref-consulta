############################################
#
#  Outro exemplo de como funciona a 
#  palavra reservada CONTINUE no Python
#
############################################

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input('Insira as vogais: ')
user_word = user_word.upper() # converte as letras para maiúscula !!!

for letter in user_word:
    # Complete the body of the for loop.
    if letter in 'AEIOU':
        continue
    else:
        print(letter)
    

