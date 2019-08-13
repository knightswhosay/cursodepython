'''
@author Mateus R. Moreira
@date 12/09/2019 

Desenvolva um programa que peça 6 números
os pares ele soma os ímpares ele desconsidera
'''

g = 0
for c in range(0,6):
    n = int(input('Escreva um número '))
    if n%2==0:
       g+=n
print(f'A soma de todos os números pares são {g}') 