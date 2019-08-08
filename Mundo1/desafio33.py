'''
@Author Mateus R. Moreira
@Date 31/07/2019

escreva um programa que peça 3 números
e diga qual é o maior e o menor
'''

n = []
n.append(int(input('Digite o primeiro número ')))
n.append(int(input('Digite o segundo número ')))
n.append(int(input('Digite o terceiro número ')))
n.sort()
resposta = f'''
{n[0]} É o menor 
{n[2]} É o meior
'''

print(resposta)