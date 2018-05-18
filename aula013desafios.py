# DESAFIOS AULA 13

# 046 Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
# indo de 0 a 10 com uma pausa de 1 segundo entre eles

from time import sleep
print('Os fogos começam em...')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('{:=^40}'.format(' FOGOS DE ARTIFÍCIO '))

# 047 crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50

for c in range(1, 26):
    print(c * 2, end=' ')

# 048 faça um programa que calcule a soma entre todos os números impares que são múltiplos de 3 e que se encontram
# no intervalo de 1 até 500

s = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
print(s)

# 049 refaça o desafio 009 mostrando a tabuada de um numero que o usuário escolher só que utilizando a estrutura for

n = int(input('Digite o número que você quer saber a tabuada: '))
print('A TABUADA DO {} É:'.format(n))
for c in range(0, 11):
    print('{} x {} ='.format(n, c), n * c)

# 050 Desenvolva um programa que leia 5 numeros inteiros e mostre a soma apenas daqueles que forem pares

s = 0
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
print(s)

# 051 Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# no final mostre os 10 primeiros termos dessa progressão

i = int(input('Digite o início de sua PA: '))
r = int(input('Digite a razão de sua PA: '))
print('Os 10 primeiros termos de sua PA são: ')
for c in range(i, 10 * r, r):
    print(c, end=' -> ')
print('Acabou')

# 052 faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo

n = int(input('Digite um número: '))
s = 0
for c in range(1, n + 1):
    if n % c == 0:
        s = s + 1
if s == 2:
    print('{} é primo!'.format(n))
else:
    print('{} não é primo!'.format(n))

# 053 crie um programa que leia uma frase e diga se é um palindromo, desconsiderando dos espaços

frase1 = input('Digite um frase: ').upper()
frase = frase1.replace(' ', '')
n = len(frase)
inversa = ''
for c in range(n-1, -1, -1):
    inversa = inversa + (frase[c])
if inversa == frase:
    print('"{}" é um palíndromo!'.format(frase1.capitalize()))
else:
    print('"{}" não é um palíndromo!'.format(frase1.capitalize()))

# 054 crie um programa que leia o ano de nascimento de 7 pessoas, no final diga quantas atingiram a maioridade
# e quantas não (maioridade = 21)

from datetime import date
s = 0
m = 0
for c in range(1, 8):
    n = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if date.today().year - n < 21:
        s = s + 1
    else:
        m = m + 1
print('{} menore(s) de idade e {} maiore(s)'.format(s, m))

# 055 faça um programa que leia o peso de 5 pessoas e mostre qual foi o maior e menor peso

m = 0
n = 0
m1 = 0
n1 = 0
for c in range(1, 6):
    p = float(input('Digite o peso em Kg da {}ª pessoa: '.format(c)))
    if c == 1:
        m = p
        n = p
        n1 = c
        n2 = c
    if p >= m:
        m1 = c
        m = p
    if p < n:
        n1 = c
        n = p
print('''A {}ª pessoa pesa {}Kg e é a mais pesada!
A {}ª pessoa pesa {}Kg e é a menos pesada!'''.format(m1, m, n1, n))

# 056 desenvolva um programa que leia nome idade e sexo de 4 pessoas
# No final o programa deve dizer a média de idade do grupo, o nome do homem mais velho e qnts mulheres tem < que 20 anos

sidade = 0
i = 0
n = ""
s = 0
for c in range(1, 5):
    nome = input('Digite o nome da {}ª pessoa: '.format(c)).capitalize()
    sexo = input('Sexo (M/F): ').upper()
    idade = int(input('Idade: '))
    sidade = sidade + idade
    if sexo == 'M' and idade > i:
        i = idade
        n = nome
    if sexo == 'F' and idade < 20:
        s = s + 1
print('''A média das idades do grupo é de {} anos.
O nome do homem mais velho é "{}".
{} mulhere(s) do grupo tem menos que 20 anos.'''.format(sidade / 4, n, s))