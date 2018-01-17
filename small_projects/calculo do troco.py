# 1[Impressão da explicação do algoritmo]
print('Bem-vindo ao nosso programa final da disciplina de Introdução à Algoritmia. Este programa pede ao utilizador um valor em cêntimos e calcula o número de moedas mínimas para obter essa quantia.')
print('O programa será executado enquanto a quantia inserida for maior do que zero.')
print('Nota: as moedas de 2 e 20 cêntimos não serão utilizadas neste programa.')
print() #linha em branco para melhorar a formatação do output

#2[Inicialização/Definição de variáveis]

#variáveis para guardar o número de cêntimos que cada moeda representa
moeda1 = 1
moeda5 = 5
moeda10 = 10
moeda50 = 50
moeda100 = 100
moeda200 = 200
#inicialização de variáveis count para guardar o número de vezes que a moeda é utilizada para calcular o resultado
count1 = 0
count5 = 0
count10 = 0
count50 = 0
count100 = 0
count200 = 0

# 3[Leitura de variáveis]
quant = int(input('Introduza a quantidade, em cêntimos: ')) #pede ao utilizador uma quantidade de cêntimos
if quant <= 0: #caso a quantidade introduzida seja negativa ou zero, o programa pede ao utilizador uma nova quantia até ser introduziada uma quantia positiva
    while (quant <= 0):
        quant = int(input('A quantia que introduziu não é válida. Por favor introduza uma quantia maior do que zero.'))

quant_calc = quant #esta variável é usada apenas durante os cálculos dentro do ciclo

#forma de calcular o resultado
# compara-se cada uma das moedas disponíves, por ordem decrescente de valor, com a variável quant_calc (que é na realidade a quantidade introduzida pelo utilizador): caso quanto_calc seja maior do a moedaX com que se está a comparar subtrai-se moedaX ao valor de quanto_calc, caso contrário testa-se a moeda seguinte. o processo é repetido até uma das comparações ser Verdadeira
# quando quanto_calc se torna igual a zero, faz-se output do resultado e questiona o utilizador se quer inserir outro valor ou não
# no caso de resposta negativa o programa faz output de uma mensagem e termina o programa; caso contrário volta reinicializa as variáveis count e quanto_calc

while quant != 0 : #ciclo para ser executado enquanto o input do utilizador não for 0
    if quant_calc >= moeda200: #testa a moeda de €2
        quant_calc -= moeda200
        count200 += 1
    elif quant_calc >= moeda100: #testa a moeda de €1
        quant_calc -= moeda100
        count100 += 1
    elif quant_calc >= moeda50: #testa a moeda de 50 cêntimos
        quant_calc -= moeda50
        count50 += 1
    elif quant_calc >= moeda10: #testa a moeda de 10 cêntimos
        quant_calc -= moeda10
        count10 += 1
    elif quant_calc >= moeda5: #testa a moeda de 5 cêntimos
        quant_calc -= moeda5
        count5 += 1
    else: #a última moeda que falta testar
        quant_calc -= moeda1 #testa a moeda de 1 cêntimo
        count1 += 1
        
    if quant_calc == 0: #verifica se quant_calc já é igual a zero
        print() #linha em branco para melhorar a formatação do output
        print('Para a quantia',quant,'são necessárias as seguintes moedas nas respetivas quantidades:')
        print('------------------------------')
        print('| Moedas de 1 cêntimo:', count1,'    |')
        print('| Moedas de 5 cêntimos:', count5,'   |')
        print('| Moedas de 10 cêntimos:', count10,'  |')
        print('| Moedas de 50 cêntimos:', count50,'  |')
        print('| Moedas de €1:', count100,'           |')
        if len(str(count200)) > 1:
            print('| Moedas de €2:', count200,'          |')
        else:
            print('| Moedas de €2:', count200,'           |')
        print('------------------------------')
        print() #linha em branco para melhorar a formatação do output

        quant = int(input('Pretende inserir outra quantia em cêntimos? Insira 0 (zero) para terminar o programa.')) #testa se o utilizador pretende inserir um novo valor
        if quant < 0: #caso a quantidade introduzida seja negativa, o programa pede ao utilizador uma nova quantia até ser introduziada uma quantia positiva
            while quant < 0:
                quant = int(input('A quantia que introduziu não é válida. Por favor introduza uma quantia maior do que zero.'))
            if quant == 0: #para resposta negativa o programa faz output de uma mensagem e termina
                confirmar = input('Tem a certeza que pretende terminar o programa? s/n') #confirma se o utilizador quer realmente terminar o programa
                if confirmar == 's': #se 's', então o progrma faz output de uma mensagem e termina
                    print() #linha em branco para melhorar a formatação do output
                    print('Escolheu terminar o programa.')
                elif confirmar == 'n': #se 'n', então o programa faz output de uma mensagem e volta a pedir ao utilizador uma quantia
                    print() #linha em branco para melhorar a formatação do output
                    print('Escolheu continuar o programa.')
                    quant = int(input('Insira outra quantia em cêntimos: '))
                    while quant <= 0:
                        quant = int(input('A quantia que introduziu não é válida. Por favor introduza uma quantia maior do que zero.'))
                    else:
                        quant_calc = quant
                    #restaura o valor inicial das variáveis diretamente após o utilizador inserir uma quantia maior do que 0; de modo a prevenir bugs
                    count1 = 0
                    count5 = 0
                    count10 = 0
                    count50 = 0
                    count100 = 0
                    count200 = 0
                    quant_calc = quant
            else:
                #restaura o valor inicial das variáveis diretamente após o utilizador inserir uma quantia maior do que 0; de modo a prevenir bugs
                quant_calc = quant
                count1 = 0
                count5 = 0
                count10 = 0
                count50 = 0
                count100 = 0
                count200 = 0
                quant_calc = quant
        else:
            if quant == 0: #para resposta negativa o programa faz output de uma mensagem e termina
                confirmar = input('Tem a certeza que pretende terminar o programa? s/n') #confirma se o utilizador quer realmente terminar o programa
                if confirmar == 's': #se 's', então o progrma faz output de uma mensagem e termina
                    print() #linha em branco para melhorar a formatação do output
                    print('Escolheu terminar o programa.')
                elif confirmar == 'n': #se 'n', então o programa faz output de uma mensagem e volta a pedir ao utilizador uma quantia
                    print() #linha em branco para melhorar a formatação do output
                    print('Escolheu continuar o programa.')
                    quant = int(input('Insira outra quantia em cêntimos: '))
                    while quant < 0:
                        quant = int(input('A quantia que introduziu não é válida. Por favor introduza uma quantia maior do que zero.'))
                    else:
                        quant_calc = quant
                    #restaura o valor inicial das variáveis diretamente após o utilizador inserir uma quantia maior do que 0; de modo a prevenir bugs
                    count1 = 0
                    count5 = 0
                    count10 = 0
                    count50 = 0
                    count100 = 0
                    count200 = 0
                    quant_calc = quant
            else: #restaura o valor inicial das variáveis diretamente após o utilizador inserir uma quantia maior do que 0; de modo a prevenir bugs
                count1 = 0
                count5 = 0
                count10 = 0
                count50 = 0
                count100 = 0
                count200 = 0
                quant_calc = quant
