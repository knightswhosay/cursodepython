'''
@author Mateus R. Moreira
@date 03/07/2019

Escreva um programa que leia 3 números e diga 
qual é o maior
'''
n1 = int(input('Digite um número '))
n2 = int(input('Digite um outro número '))
n3 = int(input('Digite mais um número '))
menor = n1
if n2 < n1 or n2 > n3:
    menor = n2
    if n2 > n3:
       menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
   maior = n3
print(f'O maior número é {maior}\nE o menor é {menor}')
'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''