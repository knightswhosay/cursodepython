'''
@author Mateus R. Moreira
@date 22/08/2019

Crie um programa que leia o nome e o preço 
de produtos e retorne o total gasto,
quantos produtos custam mais de 1000 reais
o nome do produto mais barato
'''
#inputs
nome  = str(input('Digite o nome do produto '))
preco = float(input('Digite o valor '))

# counters
total = 0
morethanK = 0
cheapest = 0

r = input('Quer continunar? [S/n] ')
while r == 's':
    nome  = str(input('Digite o nome do produto '))
    preco = int(input('Digite o valor '))
    if cheapest == 0:
       cheapest = preco
    elif cheapest > preco:
       cheapest = preco     
    total += preco
    
    if preco > 1000:
       morethanK += 1
    r = input('Quer continunar? [S/n] ')
print(f'''
Foram registrado 
um total de R${total} em compras
{morethanK} produtos custando acima de R$1000
{cheapest}  é o produto mais barato
''')