'''
@author Mateus R. Moreira
@date 26/06/2019

Escreva um programa que converta uma temperatura digitando em graus Celsius e 
converta para graus Fahrenheit.
'''
c = float(input('Digite a temperatura em Celcius C°: '))

fahrenheit = (c*1.8) + 32

print(f'{c}C° (Graus celcius) são {fahrenheit}F° (Graus fahrenheit)')