# 005 faça um programa que leia um número na tela e mostre seu sucessor e antecessor

n = int(input('Digite um número inteiro: '))
n1 = n - 1
n2 = n + 1
print('Seu antecessor é {} e seu sucessor é {}!'.format(n1, n2))

# 006 crie um algoritmo que mostre o seu dobro, triplo e raiz quadrada

n3 = n * 2
n4 = n * 3
n5 = n ** 0.5

print('Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f}'.format(n3, n4, n5))

# 007 desenvolva um programa que leia as duas notas de um aluno e depois diga sua média

nota1 = float(input('Nota primeira prova: '))
nota2 = float(input('Nota segunda prova: '))
media = (nota1 + nota2) / 2
print('Média final é {}!'.format(media))

# 008 Escreva um programa que leia o valor em metros e o converta para centimetros e milímetros

metros = float(input('Quantos metros? '))
cent = metros * 100
mili = metros * 1000
print('É igual a {} centímetros e {} milímetros!'.format(cent, mili))

# 009 Faça um programa que leia um número inteiro na tela e mostre a sua tabuada

n = int(input('Digite um número inteiro: '))
print('-' * 11)
print('{} x {:2} = {:2}'.format(n, 1, n * 1))
print('{} x {:2} = {}'.format(n, 2, n * 2))
print('{} x {:2} = {}'.format(n, 3, n * 3))
print('{} x {:2} = {}'.format(n, 4, n * 4))
print('{} x {:2} = {}'.format(n, 5, n * 5))
print('{} x {:2} = {}'.format(n, 6, n * 6))
print('{} x {:2} = {}'.format(n, 7, n * 7))
print('{} x {:2} = {}'.format(n, 8, n * 8))
print('{} x {:2} = {}'.format(n, 9, n * 9))
print('{} x {:2} = {}'.format(n, 10, n * 10))
print('-' * 11)

# 010 Conversor de moedas BRL -> USD

reais = float(input('Digite quantos reais você tem: '))
dolares = reais / 3.27
print('Você tem US$ {:.2f}'.format(dolares))

# 011 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a area e a quantidade
# e a quantidade de tinta necessária, sabento que cada litro pinta uma área de 2 m ** 2

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
tinta = area / 2
print('A área da parede é igual a {:.2f} m² e serão necessários {:.2f}L de tinta para pintá-la'.format(area, tinta))

# 012 Faça um algoritmo que leia o preço de um produto e mostre seu preço com 5% de desconto

preco = float(input('Qual o preço do produto? '))
desconto = preco * 0.95
print('O preço com desconto de 5% é de R$ {:.2f}'.format(desconto))

# 013 Faça um algoritmo que leia o salario e mostre  seu novo salário com 15% de aumento

salario = float(input('Qual é seu salário hoje? '))
aumento = salario * 1.15
print('Seu novo salário com aumento de 15% é de R$ {:.2f}'.format(aumento))

