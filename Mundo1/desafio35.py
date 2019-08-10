'''
@author Mateus R. Moreira
@date 03/07/2019

Escreva um programa que leia 3 retas e diga
se forma um triângulo ou não
'''
x = float(input('Digite a primeira reta '))
y = float(input('Digite a segunda reta '))
z = float(input('Digite a terceir reta '))
r = 'Não formam um triângulo'
if x+y>z and x+z>y and y+z>x:
    r = 'Formam um triângulo'

print(r)
'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''