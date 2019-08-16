'''
@author Mateus R. Moreira
@date 15/09/2019

Faça um programa que pegue o peso de 5 pessoas
e diga qual é o maior peso e o menor
'''
maior = 0
menor = 0
for i in range(1,6):
    n = float(input(f'Digite o peso da {i}° pessoa '))
    if n > maior:
       maior = n
       if i == 1:
        menor = n 
    if n < menor:
       menor = n
print(f'O maior peso foi {maior}KG\nO menor peso foi {menor}KG')
