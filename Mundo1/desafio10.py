'''
@author Mateus R. Moreira
@date 24/06/2019

Escreva um programa que receba um valor em real
e retorne o valor em dólares
'''
real = float(input('Digite quando você tem em Real, R$: '))
print(f'Com R${real} dá para comprar US${real/3.75:.2f}')