'''
@author Mateus R. Moreira
@date 12/09/2019 

escreva um programa que calcule a
progressão aritimética pegando a PA
'''

g = 10 

p = int(input('Escreva a proporção '))
a = int(input('Escreva a razão '))

for c in range(1,p+1,a):
    g-=1
    print(c)