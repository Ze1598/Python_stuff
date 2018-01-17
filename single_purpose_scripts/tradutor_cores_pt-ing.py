# cores e as suas traduções, para acrescentar cores é só preciso seguir o formato apresentado
blue = "azul"
red = "vermelho"
green = "verde"
yellow = "amarelo"
black = "preto"
white = "branco"

# mensagem de boas vindas e apresentação do programa
print(u"Bem vindo ao tradutor de cores de português para inglês. As cores disponíveis são azul, vermelho, verde, amarelo, preto e branco.")
# guarda o input do utilizador como a variável 'cor' para que seja comparado com as cores declaradas pelo programador
cor = str(input(u"Por favor escolha uma cor:"))

'''condição que compara o input do utilizador ('cor') com as cores declaradas pelo programador; para que o programa faça a comparação é necessário que o 
input do utilizador tenha pelo menos 1 caracter e que seja um string constituído apenas por letras'''
if len(cor) > 0 and cor.isalpha(): 
# condição para traduzir azul  
    if cor == blue:
        print(u"A tradução para inglês da cor azul é blue.")
# condição para traduzir vermelho    
    elif cor == red:
        print(u"A tradução para inglês da cor vermelho é red.")
# condição para traduzir verde    
    elif cor == green:
        print(u"A tradução para inglês da cor verde é green.")
#a partir daqui o programa assume estes elif como não fazendo parte da condição inicial por alguma razão
# condição para traduzir amarelo
    elif cor == yellow:
      print(u"A tradução para inglês da cor amarelo é yellow.")
# condição para traduzir preto	
    elif cor == black:
      print(u"A tradução para inglês da cor preto é black.")
# condição para traduzir branco	
    elif cor == white:
      print(u"A tradução para inglês da cor branco é white.")
#a partir daqui o programa assume elif adicionais como não fazendo parte da condição inicial por alguma razão
	
#caso o input do utilizador não corresponda a nenhuma das cores declaradas pelo programador, o programa apresenta a seguinte mensagem    
    else:
        print(u"Não é uma cor válida")
#caso o input do utilizador seja um string sem caracteres/vazio ou contenha caracteres que não sejam letras, o programa apresenta a seguinte mensagem
else:
	print(u"Não é uma cor válida.")