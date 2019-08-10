'''
@author Mateus R. Moreira
@date 03/07/2019

Faça um programa que leia um ano qualquer 
E mostre se ele é Bissexto
'''
from datetime import date
year = int(input('Em que ano estamos? '))
rest = f'O Ano de {year} não é um ano bissexto'

if year == 0:
   year =  date.today().year
   rest = f'O Ano de {year} não é um ano bissexto'
elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
   rest = f'O Ano de {year} é um ano bissexto'

print(rest)

'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''