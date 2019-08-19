'''
@author Mateus R. Moreira
@date 19/08/2019

Desenvolva um programa com a flag
mostre quantos números foram digitados
a soma entre eles
'''
n = int(input('Digite um número '))
s = n
c = 1
while n != 999:
    n = int(input('Digite um número '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados {c} números e o total da soma foi {s}')    