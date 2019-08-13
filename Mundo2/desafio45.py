'''
@Author Mateus R. Moreira
@Date 11/08/2019

Faça um jogo de pedra papel tesoura
'''

# Imports
from random import randint
from time import sleep

#Variables
computer = randint(1,3)
player = int(input('''
Escolha
[1] Para Pedra
[2] Para Papel
[3] Para tesoura
'''))
print(computer)
# Flow way
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')

if player == computer:
   print('Empate')
elif player == 1 and computer == 3:
    print('Você ganhou')
elif player == 2 and  computer == 1:
    print('Você ganhou')
elif player == 3 and computer == 2:
    print('Você ganhou')    
else:
    print('Computador ganhou')