'''
@Author Mateus R. Moreira
@date 31/07/2019

Escreva um programa que diga se um ano é bissexto ou não
'''
from datetime import datetime
ano = int(input('Escreva um ano, Coloque 0 para o ano atual '))

if ano == 0:
    ano = datetime.now().year

if ano%4 == 0 and ano%100!=0 or ano%400==0:
    print(f'{ano} é ano bissexto')
else:
    print(f'{ano} não é ano bissexto')

