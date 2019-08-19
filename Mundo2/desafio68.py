'''
@author Mateus R. Moreira
@date 15/09/2019

Crie um programa que jogue par ou impar
O programa só para quando o jogador perder
e quanta quantas vitórias o jogador conseguiu
'''
from random import randint

player = int(input('Escolha um número '))
v = 0
c = randint(0,10)

while True:
  escolha = str(input('Você quer impar ou par [I/P] ')).lower()  
  print(f'''
Você escolheu {player}
O computador escolheu {c}
''')
  s = player+c
  if escolha == 'i' and s%2 != 0:
     v+=1
     print('Você ganhou')
  elif escolha == 'p' and s%2 == 0:
     v+=1 
     print('Você ganhou')
  else:
     print('O computador ganhou') 
     break  
  player = int(input('Escolha um número '))

print(f'O total de vitórias foram {v}')
