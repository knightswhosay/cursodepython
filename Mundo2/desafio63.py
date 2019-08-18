'''
@author Mateus R. Moreira
@date 17/08/2019

Escreva a sequencia de fibonacci
'''
print('='*30)
print('Sequencia de Fibonacci')
n = int(input('quantos termos você quer calcular? '))

t1 = 0
t2 = 1
t3 = t1+t2
print(f'{t1} -> {t2}', end='')

while n >= 2:
    t3 = t1+t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    n -= 1
print('\n')