'''
@author Mateus R. Moreira
@date 16/08/2019

Escreva a sequencia de fibonacci
'''

fib = int(input('Escreva um número para ver sua sequencia de fibonacci '))
g = fib
while g > 0:
    if fib <= 2:
       print('-> 1 ', end='') 
       break
    print(f'0 -> 1 -> 1 -> {fib} ', end='')   
    fib = (fib - 1) + (fib - 2)
    g -= 1
print('\n')