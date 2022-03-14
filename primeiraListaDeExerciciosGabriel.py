import math
from audioop import reverse
1
x = int(input("quanto é x "))
y = int(input("quanto é y "))
z =  ((x**2) + (y**2)) / (x - y)
print(z)

2
salario = float(input("coloque seu salário: "))
print (salario + (salario)*(35/100))

3
nota1 = float(input("sua nota 1 é "))
nota2 = float(input("sua nota 2 é "))
nota3 = float(input("sua nota 3 é "))
nota4 = float(input("sua nota 4 é "))
print("suas notas são: ", nota1, nota2, nota3, nota4)
mediaNotas = (nota1 + nota2 + nota3 + nota4) / 4 
print(("sua média é ") + str(mediaNotas))

4
nomeDoProduto = input("diga qual é o produto: ")
quantidadeDoProduto = float(input("quantidade deste produto "))
valorDoProduto = float(input("qual o valor do produto? R$"))
descontoDoProduto = float(input("qual a porcentagem de desconto recebido? %"))
valorInteiro = quantidadeDoProduto * valorDoProduto
valorDoDesconto = valorInteiro * (descontoDoProduto/100)
valorComDesconto = valorInteiro - valorDoDesconto
print("O produto escolhido foi ",nomeDoProduto," e seu valor foi ", valorComDesconto)

5
Tempo = float(input("Quantos segundos levaram para você ouvir o trovão depois de vê-lo? "))
velocidadeDoTrovao = 340
distanciaDoTrovaoEmMetros = velocidadeDoTrovao * Tempo 
distanciaDoTrovaoEmKm = distanciaDoTrovaoEmMetros / 1000
print ("O trovão estava à ", distanciaDoTrovaoEmKm, " quilômetros de você!")

6
#versão em função
def valorConverter():
    valorRealFuncao = (float(input('Qual Valor você quer converter?')))
    cotacaoDolar = 5.06
    print(round(valorRealFuncao * cotacaoDolar,2))#impedir o arredondamento total do valor.
    print('O Valor Da cotação está 5.06')
valorConverter()

#versão sem função
quantosDolares = float(input("Quantos dólares você possui? $"))
cotacaoDolar = 5.06
valorReal = quantosDolares * cotacaoDolar
print("Você possui R$", valorReal, " em dólares.")
print("a atual cotação do dólar é R$",cotacaoDolar)

7
qualTempF = float(input("Indique a temperatura em Fahrenheit: "))
temperaturaCelsius = (5/9) * (qualTempF - 32)
print("A temperatura em celsius é de", temperaturaCelsius)

8
Real = (int(input('Insira um valor inteiro em reais: ')))
valorReduzidoCem = ((Real-(Real//100)*100))//50#Essa linha divide o valor inputado por 100 e pega o resto, multiplica o decimal por 100 e pega o resto da divisão por 50
valorReduzidoCinquenta = ((Real-((Real//100)*100))-(valorReduzidoCem*50))//10#subtrai do resto maior ou menor que 50 para obter as notas de 10
valorReduzidoDez =  ((((Real-((Real//100)*100))-(valorReduzidoCem*50)))-valorReduzidoCinquenta*10)//1#Essa linha faz o mesmo, porém agora para obter as notas de 1
if (Real) < 100:
    print('Precisarás de 0 notas de 100 reais')
    print(f'Precisarás de {valorReduzidoCem} notas de 50 reais')
    print(f'Precisarás de {valorReduzidoCinquenta} notas de 10 reais')
    print(f'Precisarás de {valorReduzidoDez} moedas de 1 real')
elif (Real) >= 100:
    print('Precisarás de ', Real//100, 'notas de 100 reais!')
    print(f'Precisarás de {valorReduzidoCem} notas de 50 reais')
    print(f'Precisarás de {valorReduzidoCinquenta} notas de 10 reais')
    print(f'Precisarás de {valorReduzidoDez} moedas de 1 real')

9
umaFrase = str(input("Escreva a frase que deverá ser formatada: "))
caracteresParaSubstituir = " "
for u in range(len(caracteresParaSubstituir)):#repetirá a ação até todos os espaços serem apagados.
    umaFrase = umaFrase.replace(caracteresParaSubstituir[u], "")#irá substituir os espaços entre as palavras por vazio, concatenando as palavras.
print(umaFrase.upper())

10
primeiraPalavraMistura = str(input("Qual palavra você deseja misturar? "))
segundaPalavraMistura = str(input("Que outra palavra desejas misturar? "))
listaPrimeiraPalavra = list(primeiraPalavraMistura)#transforma em lista(array)
listaSegundaPalavra = list(segundaPalavraMistura)
metadeDaPrimeiraPalavra = int((math.floor(((len(primeiraPalavraMistura))/2)-1)))#pega a letra do meio da 1º palavra
metadeDaSegundaPalavra = int((math.floor(((len(segundaPalavraMistura))/2)-1)))
inicioDaPalavra = 0
fimDaPalavra = -1
tresPrimeirasLetras1 = (listaPrimeiraPalavra.pop(inicioDaPalavra) + listaPrimeiraPalavra.pop(metadeDaPrimeiraPalavra) + listaPrimeiraPalavra.pop(fimDaPalavra))
tresPrimeirasLetras2 = (listaSegundaPalavra.pop(inicioDaPalavra) + listaSegundaPalavra.pop(metadeDaSegundaPalavra) + listaSegundaPalavra.pop(fimDaPalavra))
print (tresPrimeirasLetras1 + tresPrimeirasLetras2)

11
fraseDeBase = str(input("Qual a situação do covid19 na su sua cidade? "))
quantosCovid = fraseDeBase.upper().count("covid19".upper())#irá contar todas as ocorrências de covid19 na frase, estando maiusculas ou minusculas.
print("A frase "+ fraseDeBase +" contem ", quantosCovid, " ocorrencias da palavra covid19.")

12
valorNUm = float(input("Qual numero você deseja utilizar? "))
valorNDois = float(input("Que outro numero você deseja utilizar? "))
expressaoSoma = valorNUm + valorNDois
expressaoSubtracao = valorNUm - valorNDois
expressaoMultiplicacao = valorNUm * valorNDois
expressaoDivisao = valorNUm / valorNDois
horaDaConta = input("Qual conta deseja realizar? ")
if horaDaConta.lower() == ('somar'):
    print("O resultado da sua soma foi " , expressaoSoma)
elif horaDaConta.lower() == ('subtrair'):
    print("O resultado da sua subtração foi " , expressaoSubtracao)
elif horaDaConta.lower() == ('multiplicar'):
    print("O resultado da sua multiplicação foi " , expressaoMultiplicacao)
elif horaDaConta.lower() == ('dividir'):
    print("O resultado da sua divisão foi " , expressaoDivisao)

13
segundosDefinidos = int(input("Quantos segundos queres converter? "))
totalHoras = segundosDefinidos // 3600
sobraSegundos = segundosDefinidos % 3600#pega o resto da quantidade de segundos dividido por 3600
totalMinutos = sobraSegundos // 60
totalSegundos = sobraSegundos % 60#pega o resto do resto para obter os segundos
print(f'O correspondente em horas, minutos e segundos é: {totalHoras}:{totalMinutos}:{totalSegundos}.')

14
sucoDeLaranja = "Isto é suco de laranja"
if sucoDeLaranja.count('laranja') >= 1:
    print("SIM, HÁ A PALAVRA LARANJA")

15
descubraOTamanhoDaSuaString = str(input("Escreva qualquer coisa aí, jóia? "))
tamanhoDaString = len(descubraOTamanhoDaSuaString)
print(f" sua string possui {tamanhoDaString} caracteres.")

16
primeiroCateto = int(input("Qual o primeiro cateto de nosso triangulo? "))
segundoCateto = int(input("Qual o segundo cateto desse triangulo? "))
hipotenusa = float(((primeiroCateto**2) + (segundoCateto**2))**0.5)#Eu decidi usar elevação na potencia de 0.5 para equivaler a hipotenusa ao quadrado
print(round(hipotenusa, 2))

17
ladoAbTriangulo = int(input("Qual o tamanho do lado AB deste triangulo? "))
ladoBcTriangulo = int(input("Qual o tamanho do lado BC deste triangulo? "))
ladoAcTriangulo = int(input("Qual o tamanho do lado AC deste triangulo? "))
if ladoAbTriangulo == ladoBcTriangulo == ladoAcTriangulo:
    True
    print("Parabéns, seu lindo triangulo é equilátero!!")
elif ladoAbTriangulo == ladoBcTriangulo != ladoAcTriangulo or ladoAcTriangulo == ladoBcTriangulo != ladoAbTriangulo or ladoAbTriangulo == ladoAcTriangulo != ladoBcTriangulo:
    False
    print("Lamento lhe informar, seu triangulo não é equilátero, mas é isósceles!!")
else:
    False
    print("Seu triangulo é completamente assimétrico.")

18
numerosLimpos = str(input("Escolha cinco numeros inteiros que serão listados: "))
caracteresIndesejados = " ", ",", ".", ":"
for i in range(len(caracteresIndesejados)):
    numerosLimpos = numerosLimpos.replace(caracteresIndesejados[i], '')
numeroIndice = list(numerosLimpos)
indices = 0
indice0 = numeroIndice.pop(indices) + " no primeiro índice,"
indice1 = numeroIndice.pop(indices) + " no segundo índice,"
indice2 = numeroIndice.pop(indices) + " no terceiro índice,"
indice3 = numeroIndice.pop(indices) + " no quarto índice,"
indice4 = numeroIndice.pop(indices) + " no quinto índice."
print(indice0,indice1,indice2,indice3,indice4)

19
quaisNotas = (input("Quais foram as quatro suas notas? "))
print(f"Suas notas são: {quaisNotas}")
caracteresIndesejados = " ", ",", ".", ":"
for i in range(len(caracteresIndesejados)):
    quaisNotas = quaisNotas.replace(caracteresIndesejados[i], '')
todasNotas = list(quaisNotas)
retirarNotas = todasNotas.pop(0)
primeiraNota = int(retirarNotas)
segundaNota = int(retirarNotas)
terceiraNota = int(retirarNotas)
quartaNota = int(retirarNotas)
mediaTotalNotas = (primeiraNota + segundaNota + terceiraNota + quartaNota)/4
mediaFinal = round(mediaTotalNotas,2)
todasNotasString = str(todasNotas)
print(f"Sua média é {mediaFinal}.")

20
informeIdadeAltura = (input("Coloque aqui a idade e altura de 5 amigos seu, separando-os com '/': "))
idadeAlturaLista = informeIdadeAltura.split('/')
amigoUm = idadeAlturaLista.pop(0)
amigoDois = idadeAlturaLista.pop(0)
amigoTres = idadeAlturaLista.pop(0)
amigoQuatro = idadeAlturaLista.pop(0)
amigoCinco = idadeAlturaLista.pop(0)
print(f"Seu amigo cinco:{amigoCinco}, amigo quatro: {amigoQuatro}, amigo tres: {amigoTres}, amigo dois: {amigoDois}, amigo um:{amigoUm}")

21
stringNumeroUm = (input("Coloque quantos numeros inteiros quiser: "))
stringNumeroDois = (input("Coloque quantos numeros inteiros quiser: "))
caracteresIndesejados = " ", ",", ".", ":"
for i in range(len(caracteresIndesejados)):
    stringNumeroUm = stringNumeroUm.replace(caracteresIndesejados[i], '')
    stringNumeroDois = stringNumeroDois.replace(caracteresIndesejados[i], '')
listaNumeroUm = list(stringNumeroUm)
listaNumeroDois = list(stringNumeroDois)
listaNumeroTres = listaNumeroUm + listaNumeroDois
listaNumeroTres.sort(reverse=True)
print(listaNumeroTres)

22
nomeDefinido = str(input("Que nome deve ser contado? "))
listaDeNomes = [
    'gabriel','yuri','anderson','leandro','ana','julia','jorge','helena','arthur','vitoria','debora','bruna','nicolas','sandro','otavio','marcelo','joao','maria','jose',
    'gabriela','yuri','anderson','leandro','ana','julio','jorge','helena','arthur','vitor','debora','bruno','nicolas','sandro','otavia','marcela','joao','mario','jose',
    'gabriel','yuri','anderson','leandro','ana','julia','jorge','heleno','arthur','vitoria','debora','bruna','nicolas','sandro','otavio','marcelo','joao','maria','jose',
]
aparicaoDosNomes = f"aparece {listaDeNomes.count(nomeDefinido)} vezes na lista."
dicionarioNomes = {nomeDefinido : aparicaoDosNomes }
print(dicionarioNomes)

23
informeSeuNome = str(input("Qual seu nome? "))
informeSuaIdade = int(input("Qual sua idade? "))
informeSeuCPF = str(input("Por fim, informe seu CPF: "))
dicionarioCadastro = {'nome' : informeSeuNome, 'idade' : informeSuaIdade, 'CPF' : informeSeuCPF}
acessarInformacoes = str(input('Qual informação você quer acessar? '))
if acessarInformacoes == 'CPF':
    print(f"Seu CPF é {informeSeuCPF}")
elif acessarInformacoes == 'idade':
    print(f"Sua idade é {informeSuaIdade}")
elif acessarInformacoes == 'nome':
    print(f'Seu nome é {informeSeuNome}')