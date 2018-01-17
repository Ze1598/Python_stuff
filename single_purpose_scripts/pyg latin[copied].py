# sufixo que vai ser adicionado à palavra introduzida pelo utilizador
pyg = 'ay'

# input do utilizador com a palavra da sua escolha
original = raw_input('Enter a word:')
# transformação do input do utilizador numa nova variable que contém apenas minúsculas
original = original.lower()
word = original
# variable que guarda apenas o primeiro caracter do input do utilizador
first = word[0]

# criação da variable final que consiste no input do utilizador apenas a partir do segundo caracter, o primeiro caracter do input do utilizador e o sufixo usado neste tradutor
new_word = word[1:] + first + pyg

# condição final que apresenta a tradução do input do utilizador através do PygLatin; este input tem de ter pelo menos 1 caracter e conter apenas letras
if len(original) > 0 and original.isalpha():
    print new_word
else:
    print 'empty'