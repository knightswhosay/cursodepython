'''
@author Mateus R. Moreira
@date 16/08/2019


escreva um programa que calcule a
progressão aritimética pegando a PA
mostrando os 10 primeiros termos
'''

g = 10
termo = float(input('Escreva o termo '))
razao = float(input('Escreva a razão '))
while g >= 0:
   print(f'{termo} -> ', end='')
   termo += razao 
   g -= 1
   if g == 0:
    g = int(input('\nQuantas progreções você quer ver mais? '))
print('\nAcabou!!')