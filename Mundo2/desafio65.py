'''
@author Mateus R. Moreira
@date 19/08/2019

Escreva um programa que leia vários números
e escreva a média de cada número e diga qual foi o maior
e qual foi o menor
'''

media = maior = menor = c = 0
question = 's'
while question != 'n':
    n = int(input('Digite um número '))
    media += n
    if n > maior:
       maior = n
    if c == 0:
       menor = n     
    question = str(input('Quer continuar? [S/n] ')).lower()
    c += 1
print(f'''
A média apresentada foi {media/c}
O maior número foi {maior}
O menor número foi {menor}
''')
