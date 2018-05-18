# 022 Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1) O nome com todas as letras maiúsculas
# 2) O nome com todas as letras minúsculas
# 3) Quantas letras sem considerar espaços
# 4) Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
print('Nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('Nome com todas as letras minúsulas: {}'.format(nome.lower()))
nome1 = nome.replace(" ", "")
print('Número de letras no primeiro nome: {}'.format(len(nome1)))
primeironome = nome.split()[0]
print('Número de letras no primeiro nome: {}'.format(len(primeironome)))

# 023 Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
# ex: 1896 ---> u = 6 d = 9 c = 8 m = 1

ano = input('Digite ano de 0 a 9999: ')
u = int(ano) // 1 % 10
print('Unidade =', u)
d = int(ano) // 10 % 10
print('Dezena =', d)
c = int(ano) // 100 % 10
print('Centena =', c)
m = int(ano) // 1000 % 10
print('Milhar =', m)

# 024 Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome 'SANTO'

cidade = input('Nome da uma cidade: ')
cinco = cidade[0:5].upper()
teste = cinco == 'SANTO'
print('Cidade começa com santo: {}'.format(teste))

# 025 Crie um programa que leia o nome de uma pessoa e se tem 'Silva' no nome

nome = input('Digite seu nome: ')
silva = nome.find('Silva')
teste = silva > -1
print('Nome tem Silva: {}'.format(teste))

# 026 Faça um programa que leia um frase e diga quantas vezes aparece a letra a
# Em que posição ela aparece na primeira vez e na ultima vez

frase = input('Digite uma frase: ').lower()
a = frase.count('a')
print('A letra a aparece {} vezes.'.format(a))
print('Posição Primeiro A:', frase.find('a'))
print('Posição Último A:', frase.rfind('a'))

# 027 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e segundo nome (nome, sobrenome)

nome = input('Digite seu nome: ')
print('Primeiro nome: {}'.format(nome.split()[0]))
print('Sobrenome: {}'.format(nome.split()[-1]))


