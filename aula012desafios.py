# 036 escreva um programa para aprovar o emprestimo de uma casa
# o programa vai perguntar o valor da casa, o salário do comprador e o prazo
# calcule o valor da prestação mensal sabendo que se exceder 30% do salario ele sera negado

valor = float(input('Insira o valor do bem em R$: '))
salario = float(input('Insira o salário do solicitante em R$: '))
prazo = float(input('Insira o prazo do empréstimo em meses: '))
pmt = valor / prazo
if pmt / salario > 0.30:
    print('A parcela é de R$ {:.2f}. Desculpe! Seu empréstimo foi negado.'.format(pmt))
else:
    print('A parcela é de R$ {:.2f}. Parabéns! Seu empréstimo foi aprovado!'.format(pmt))

# 037 escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão (1 para binário, 2 para octal e 3 para hexadecimal)

n = int(input('Digite o número que deseja converter: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Digite o número de sua opção: '))
if opcao == 1:
    print('{} convertido em binário é igual a {}.'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido em octal é igual a {}.'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido em hexadecimal é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Número da opção escolhida não é válido.')

# 038 escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela um mensagem
# O primeiro valor é maior ou menor ou igual

n1 = int(input('Insira um número inteiro: '))
n2 = int(input('Insira outro número inteiro: '))

if n1 > n2:
    print('O primeiro valor é maior!')
elif n1 < n2:
    print('O primeiro valor é menor!')
else:
    print('Os dois valores são iguais!')

# 039 faça um programa que leia o ano de nascimento e informe de acordo com a idade:
# 1) Se ele ainda vai se alistar no exercito
# 2) se é hora de se alistar
# 3) se já passou
# o programa deve mostrar o tempo que falta

import datetime
ano = int(input('Insira o ano de nascimento: '))
idade = 18
ali = datetime.date.today().year - ano
if ali == idade:
    print('Esse é o ano de seu alistamento!')
elif ali < idade:
    print('Falta(m) {} ano(s) para você se alistar!'.format(idade - ali))
else:
    print('Você se alistou faz {} anos!'.format(ali - idade))

# 040 crie um programa que leia duas notas de um aluno e diga se foi reprovado, esta em recuperação ou aprovado

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua média final é {:.2f}. Você está reprovado!'.format(media))
elif 7.0 > media >= 5.0:
    print('Sua média final é {:.2f}. Você está em recuperação!'.format(media))
else:
    print('Sua média final é {:.2f}. Parabéns! Você foi aprovado!'.format(media))

# 041 leia ano de nascimento e mostre categoria

import datetime
ano = int(datetime.date.today().year)
nasci = int(input('Digite o ano de nascimento: '))
idade = ano - nasci
if idade <= 9:
    print('Categoria MIRIM!')
elif idade <= 14:
    print('Categoria INFANTIL!')
elif idade <= 19:
    print('Categoria JUNIOR!')
elif idade <= 25:
    print('Categoria SÊNIOR!')
else:
    print('Categoria MASTER!')

# 042 refaça o exercício 35 dizendo que tipo de triangulo é

r1 = float(input('Digite o comprimento R1: '))
r2 = float(input('Digite o comprimento R2: '))
r3 = float(input('Digite o comprimento R3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos formam um TRIÂNGULO!')
    if r1 == r2 == r3:
        print('O triângulo é equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é isósceles!')
    else:
        print('O triângulo é escaleno!')
else:
    print('Os segmentos não podem formar um TRIÂNGULO!')

# 043 calcula IMC em que faixa está

altura = float(input('Digite sua altura em metros: '))
massa = float(input('Digite seu peso em Kg: '))
imc = massa / (altura**2)
if imc < 18.5:
    print('Seu IMC é de {:.2f}. Você está abaixo  do peso ideal!'.format(imc))
elif imc < 25:
    print('Seu IMC é de {:.2f}. Você está no peso ideal!'.format(imc))
elif imc < 30:
    print('Seu IMC é de {:.2f}. Você está com sobrepeso!'.format(imc))
elif imc < 40:
    print('Seu IMC é de {:.2f}. Você está obeso!'.format(imc))
else:
    print('Seu IMC é de {:.2f}. Você tem obesidade mórbida!'.format(imc))

# 044 calcule o valor  a ser pago e preço normal e condição de pagamento

preco = float(input('Digite o preço do produto: R$ '))
print('Escolha uma opção de pagamento:')
print('1 - Dinheiro ou cheque 1x')
print('2 - No cartão 1x')
print('3 - No cartão 2x')
print('4 - No cartão 3x ou mais')
opcao = int(input('Digite o número da opção escolhida: '))
if opcao == 1:
    print('Para essa opção o valor fica R$ {:.2f}!'.format(preco * 0.90))
elif opcao == 2:
    print('Para essa opção o valor fica R$ {:.2f}!'.format(preco * 0.95))
elif opcao == 3:
    print('Para essa opção o valor fica R$ {:.2f}!'.format(preco))
elif opcao == 4:
    print('Para essa opção o valor fica R$ {:.2f}!'.format(preco * 1.20))
else:
    print('Opção não encontrada!')

# 045 crie um programa que faça jogar pedra, papel ou tesoura

from random import choice
print('{:=^80}'.format(' JO KEN PO '))
opcao = input('''Pedra, papel ou tesoura?
''').upper()
jok = ['PEDRA', 'PAPEL', 'TESOURA']
comp = choice(jok)
if (opcao == 'PEDRA' and comp == 'TESOURA') or (opcao == 'PAPEL' and comp == 'PEDRA') \
    or (opcao == 'TESOURA' and comp == 'PAPEL'):
    print('O computador escolheu {}. {} ganha disso. Parabéns! Você ganhou!'.format(comp, opcao))
elif (opcao == 'TESOURA' and comp == 'PEDRA') or (opcao == 'PEDRA' and comp == 'PAPEL') \
    or (opcao == 'PAPEL' and comp == 'TESOURA'):
    print('O computador escolheu {}. {} perde disso. Você perdeu!'.format(comp, opcao))
elif opcao == comp:
    print('O computador também escolheu {}. Deu empate!'.format(comp))
else:
    print('Digite a opção corretamente!')
print('{:=^80}'.format(' JO KEN PO '))

