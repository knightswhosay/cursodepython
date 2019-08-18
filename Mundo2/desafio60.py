'''
@author Mateus R. Moreira
@date 17/09/2019


Faça um programa que calcule o factorial
'''

n = int(input('Escre um número para calcular o factorial '))
fac = n
c = n
while c != 0:
    fac *= c
    print(f'{fac}..', end='')
    c-=1

print(f'O factorial de {n} = {fac}')