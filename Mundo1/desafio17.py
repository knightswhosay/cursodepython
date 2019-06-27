'''
@author Mateus R. Moreira
@date 26/06/2019

Faça um programa que leia o 
cateto oposto e cateto adjacente 
e calcule a hipotenusa
'''
from math import sqrt

co = float(input('Cateto oposto '))
cd = float(input('Cateto Adjacente '))
hipotenusa = (co**2) + (cd**2)

print(f'A soma do Cateto oposto {co}² com o Cateto Adjacente {cd}² igual a = {sqrt(hipotenusa):.2f} hipotenusa')

'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''