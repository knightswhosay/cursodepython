'''
@author Mateus R. Moreira
@date 13/09/2019

Crie um programa que diga se a sua frase é um palindromo
'''

frase = str(input('Escreva um frase ')).split()
frase = ''.join(frase)
if frase[::-1].lower() == frase.lower():
   print('Temos um palindromo') 
else:
   print('Não temos um palindormo') 