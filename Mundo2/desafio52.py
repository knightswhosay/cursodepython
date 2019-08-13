'''
@author Mateus R. Moreira
@date 13/09/2019

Faça um programa que diga se os números são
ímpares ou pares
'''

g = 0
n = int(input('Escreva um número '))
for c  in range(1, n+1):
    if n%c==0:
       print('\033[31m', end=' ') 
       g+=1
    else:
       print('\033[33m', end=' ')         
    print('{}'.format(c), end=' ')

if g <= 2:
   print(f'\033[m O número {n} é um número primo\n')
else:   
   print(f'\033[m O número {n} não é um número primo\n')    