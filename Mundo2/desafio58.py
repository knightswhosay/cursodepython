'''
@author Mateus R. Moreira
@date 17/09/2019

Melhore o jogo do desafio 28
e diga quantos palpites foram necessários
'''

from random import randint
numero = randint(0,10)
userinput = int(input(':> Pensei um número entre 0-10 tente descobrir '))
result = 'você errou '
counter = 0

while numero != userinput:
    counter += 1
    userinput = int(input(f':> {result} você errou tente novamente Numeros entre 0-10 '))
if numero == userinput:
    counter += 1
    result  = f'Você acertou foram necessárioas {counter} tentativas'


print(result)
