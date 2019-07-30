'''
@Author Mateus R. Moreira
30/08/2019

Faça um programa que peça dois números 
E diga qual deles é o maior, o menor ou se são iguais
'''

n1 = int(input('Escreva o primeiro nome '))
n2 = int(input('Escreva mais outro número '))

if n1>n2:
    print(f'{n1} é o maior\n{n2} é o menor')
elif n1<n2:
    print(f'{n2} é o maior\n{n1} é o menor')
else:
    print('Ambos os números são iguais')