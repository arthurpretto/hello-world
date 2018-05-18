# 028 Faça um programa que pense num numero de 0 a 5 e peça para o usuário chutar esse numero
# se acertar 'parabens', se errar 'o computador venceu'
import calendar
from random import randint
comp = randint(0, 5)
user = int(input('Tente acertar o número de 0 a 5 que o computador está pensando: '))
if comp == user:
    print('Parabéns! Você acertou. O número pensado pelo computador é mesmo {}.'.format(comp))
else:
    print('Você errou! O número que o computador pensou foi {}.'.format(comp))

# 029 escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado
# A multa ira custar R$ 7 por cada km acima do limite

v = int(input('A velocidade o carro era (em km/h): '))
multa = float((v - 80) * 7)
if v > 80:
    print('Você foi multado! O valor da multa é de R$ {:.2f}.'.format(multa))
else:
    print('Você estava dentro do limite de velocidade')

# 030 crie um programa que leia um numero inteiro e diga se ele é par ou impar

n = int(input('Digite um número inteiro: ')) % 2
if n == 0:
    print('O número é par!')
else:
    print('O número é impar!')

# 031 Determine um programa que peça a distância da viagem
# Calcule o preço da passagem sendo que para viagens acima de 200 km a passagem é 0,45 por km e para menor é 0,5

dist = float(input('Digite a distância da viagem em km: '))
if dist >= 200:
    passagem = dist * 0.45
    print('O valor da passagem é de R$ {:.2f}'.format(passagem))
else:
    passagem = dist * 0.50
    print('O valor da passagem é de R$ {:.2f}'.format(passagem))

# 032 Faça um programa que leia um ano qualquer e mostre se ele é bissexto

from calendar import isleap
ano = isleap(int(input('Digite um ano para saber se é bissexto: ')))
if ano:
    print('Ano bissexto!')
else:
    print('Ano não é bissexto!')

# 033 faça um programa que leia 3 numeros e diga qual o maior e qual o menor

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um terceiro número: '))
lista = [n1, n2, n3]
maxi = max(lista)
mini = min(lista)
print('O maior número é {} e o menor é {}.'.format(maxi, mini))

# 034 escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
# para salários superiores a 1250 calcule um aumento de 10% e para os <= um aumento de 15%

salario = float(input('Digite seu salário em R$: '))
if salario > 1250:
    novo = salario * 1.10
    print('Seu novo salário é R$ {:.2f}!'.format(novo))
else:
    novo = salario * 1.15
    print('Seu novo salári é R$ {:.2f}!'.format(novo))

# 035 Desenvolva um progrma que leia o comprimento de 3 retas e diga se é possivel formar um triangulo

r1 = float(input('Digite o comprimento R1: '))
r2 = float(input('Digite o comprimento R2: '))
r3 = float(input('Digite o comprimento R3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos formam um TRIÂNGULO!')
else:
    print('Os segmentos não podem formar um TRIÂNGULO!')

















