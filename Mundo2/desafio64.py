'''
@author Mateus R. Moreira
@date 17/08/2019

Escreva um programa que leia
o valor digitado pelo usuário só pare 
se ele escrever 999
'''
n = c = g = 0
n = int(input('Escreve um número '))
while n != 999:
    g += n 
    c += 1
    n = int(input('Escreve um número '))
print(f'você digitou {c} e o total deu {g}')