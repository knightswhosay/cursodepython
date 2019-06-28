'''
@author Mateus R. Moreira
@date 27/06/2019

Faça um programa que peça um número entre 
1 e 9999 e diga quantas dezenas tem centenas, 
dezenas e unidades
'''

numero = int(input('Digite um número entre 1 e 9999 '))

print(f"""
 Existem:
  {numero//1000%10} Milhares
  {numero//100%10} Centenas
  {numero//10%10} Dezenas
  {numero//1%10} Unidades
"""
)
'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''