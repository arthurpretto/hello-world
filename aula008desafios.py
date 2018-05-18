# 016 crie um programa que leia um numero real qualquer pelo teclado e mostre sua porção inteira

from math import trunc
n = float(input('Digite um número não inteiro: '))
print('A parte inteira de {} é {}'.format(n, trunc(n)))

# 017 faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# calcule e mostre o comprimento da hipotenusa

from math import hypot
oposto = float(input('Digite o comprimento (m) do cateto oposto: '))
adjacente = float(input('Digite o comprimento (m) do cateto adjacente: '))
print('O valor da hipotenusa é {:.2f} metros!'.format(hypot(oposto, adjacente)))

# 018 faça um programa que leia um angulo e de o valor de seu seno, cosseno e tangente

from math import cos, sin, tan, radians
angulo = float(input('Digite um angulo em graus: '))
radiano = radians(angulo)
print('Para {:.2f}º o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(angulo, cos(radiano), sin(radiano), tan(radiano)))

# 019 um professor quer sortear um de seus 4 alunos para apagar o quadro faça um programa que escreva o nome sorteado

import random
a1 = 'Arthur'
a2 = 'Ana'
a3 = 'Cleo'
a4 = 'Cícero'
ordem = (a1, a2, a3, a4)
seq = random.choice(ordem)
print('O aluno sorteado é {}!'.format(seq))

# 020 um professor qer sortear a ordem de apresentação de seus 4 alunos

from random import shuffle
a1 = 'Arthur'
a2 = 'Ana'
a3 = 'Claudio'
a4 = 'Roberta'
list = [a1, a2, a3, a4]
shuffle(list)
print('A ordem de apresentação será:')
print(list)

# 021 faça um programa em python que abra e reproduza um arquivo em MP3

import pygame
pygame.init()
pygame.mixer.music.load('nomedoarquivo.mp3')
pygame.mixer.music.play()
pygame.event.wait()

