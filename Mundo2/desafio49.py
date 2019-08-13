'''
@author Mateus R. Moreira
@date 12/09/2019 
Peça um número e escreva sua tabuada de 0 - 10
Usando o laço for
'''

numero = int(input('Escreva um número para ver sua tabuada '))
for c in range (0,11):
  resultado = f'{c} x  {numero} = {numero*c}' 
  print(resultado)