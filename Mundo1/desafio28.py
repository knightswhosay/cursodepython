'''
@author Mateus R. Moreira
@date 28/06/2019

Faça um programa que faça o computador-
pensar em um número aleatório entre 1-5
Depois peça para o usuário digitar o número
e diga se ele acertou ou não.
'''
from random import randint
numero = randint(0,5)
userinput = int(input(':> Pensei um número entre 0-5 tente descobri '))
result = 'você errou '
if numero == userinput:
    result  = 'Você acertou'

print(result)

'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''