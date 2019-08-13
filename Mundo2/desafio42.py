'''
@Author Mateus R. Moreira
@Date 10/08/2019

Escreva um programa que diga se o triângulo é
Isósceles, Equilátero ou escaleno
'''

r1 = float(input('O primeiro segmento '))
r2 = float(input('O segundo segmento '))
r3 = float(input('O terceiro segmento '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('For um triângulo ', end='')
    if r1 == r2 == r3:
      print('Um triângulo Equiátero\n')
    if r1 != r2 != r3 != r1:
      print('Um triângulo Isósceles\n')    
    else:
      print('Um triângulo Escaleno\n')
else:
    print('Não forma um triângulo') 
