# 057 faça programa que leia o sexo de uma pessoa, caso alguem digite errado peça a digitaçao até ter o valor correto

sexo = input('Qual o seu sexo [M/F}? ').upper()
while sexo != 'M' and sexo != 'F':
    print('Por favor! Digite M se masculino ou F se feminino!')
    sexo = input('Qual o seu sexo [M/F}? ').upper()
print('Seu sexo é {}.'.format(sexo))

# 058 melhore o desafio 28 só que agora o usuário vai tentar até acertar

from random import randint
comp = randint(0, 10)
user = int(input('Tente acertar o número de 0 a 10 que o computador está pensando: '))
tent = 1
while user != comp:
    user = int(input('Tente novamente: '))
    tent = tent + 1
print('Parabéns! Você acertou em {} tentativas. O número pensado pelo computador é mesmo {}.'.format(tent, comp))

# 059 crie um programa que leia 2 valores e mostre um menu na tela:
'''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair'''

# 059 crie um programa que leia 2 valores e mostre um menu na tela: somar, multiplocar, numero >, novo n, sair

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = int(input('''Você deseja:
[ 1 ] SOMAR
[ 2 ] MULTIPLCAR
[ 3 ] INFORMAR O NÚMERO MAIOR
[ 4 ] DIGITAR NOVOS NÚMEROS
[ 5 ] SAIR
'''))
while opcao == 0 or opcao > 5:
    opcao = int(input('Digite uma opção válida: '))
    while 0 < opcao < 5:
        if opcao == 1:
            print('A soma entre {} e {} é igual a {}.'.format(n1, n2, n1 + n2))
            opcao = int(input('O que deseja fazer agora? '))
        elif opcao == 2:
            print('O produto entre {} e {} é igual a {}.'.format(n1, n2, n1 * n2))
            opcao = int(input('O que deseja fazer agora? '))
        elif opcao == 3:
            if n1 > n2:
                print('{} é maior que {}.'.format(n1, n2))
                opcao = int(input('O que deseja fazer agora? '))
            elif n1 == n2:
                print('{} é igual que {}.'.format(n1, n2))
                opcao = int(input('O que deseja fazer agora? '))
            else:
                print('{} é maior que {}.'.format(n2, n1))
                opcao = int(input('O que deseja fazer agora? '))
        if opcao == 4:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            opcao = int(input('O que deseja fazer agora? '))
print('Programa encerrado!')

# 060 faça um programa que leia um numero qualquer e mostre seu fatorial

n = int(input('Digite o número que deseja saber seu fatorial: '))
n0 = n
c = n - 1
while c != 0:
    n = n * c
    c = c - 1
print('Fatorial de {} é {}.'.format(n0, n))

# 061 refaça o exercicio 51 usando while (lendo PA com primeiro termo e razao mostrar os 10 primeiros termos)

n = int(input('Digite o primeiro termo de sua PA: '))
r = int(input('Digite a razão de sua PA: '))
c = 0
print('Sua PA é igual a:')
while c != 10:
    if c < 9:
        print(n, end=', ')
    else:
        print(n + r)
    n = n + r
    c = c + 1

# 062 melhore o desafio anterior perguntando se o usuário quer que mostre mais termos e pare quando o usuário pedir

n = int(input('Digite o primeiro termo de sua PA: '))
r = int(input('Digite a razão de sua PA: '))
c = 0
print('Sua PA é igual a:')
while c != 10:
    if c < 9:
        print(n, end=', ')
    else:
        print(n + r)
    n = n + r
    c = c + 1
mais = int(input('Você quer ver mais quando quantos termos? '))
while mais > 0 and c != 10 + mais:
    if c < 9 + mais:
        print(n, end=', ')
    else:
        print(n + r)
    n = n + r
    if c == 9 + mais:
        mais = mais + int(input('Mais quantos termos? '))
    c = c + 1

# 063 escreva um programa que leia um numero inteiro n e mostre os n primeiros numeros da sequencia de fibonacci

n = int(input('Quantos termos da sequência de Fibonacci deseja ver? '))
fib1 = 0
fib2 = 1
c = 1
while c < n:
    if fib1 == 0:
        print(fib2, end='-> ')
    print(fib2 + fib1, end='-> ')
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    c = c + 1
print(' Acabou!')

# 064 crie um programa que leia varios numeros inteiros e pare quando for digitado 999
# no final mostre a soma dos numeros inteiros (-999) e quantos foram digitados

n = int(input('Digite um número inteiro: '))
c = 0
n1 = 0
s = n
while n1 != 999:
    n1 = int(input('Digite outro número inteiro (999 para sair): '))
    s = s + n1
    c = c + 1
print('Foram digitados {} números e a soma deles é igual a {}.'.format(c, s - 999))

# 065 crie um programa que leia varios numeros inteiros pelo teclado
# no final mostre a média, qual o valor maior, qual o menor e se o usuário quer o não continuar

n = int(input('Digite um número: '))
c = 1
sair = 'S'
min = n
max = n
m = 0
while sair == 'S':
    n1 = int(input('Digite outro valor: '))
    c = c + 1
    if c == 2:
        m = (n + n1) / c
    else:
        m = ((m * (c - 1)) + n1) / c
    print('A média é {}.'.format(m))
    if n1 > max:
        max = n1
    print('{} é o maior valor digitado.'.format(max))
    if n1 < min:
        min = n1
    print('{} é o menor valor digitado.'.format(min))
    n = n1
    sair = input('Deseja continuar [S/N]? ').upper()


