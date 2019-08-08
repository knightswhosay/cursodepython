'''
@Author Mateus R. Moreira
@Date 31/07/2019

Escreva um programa que peça o salário de um funcionário
e aplique um reajuste salarial para salários abaixo de R$ 1250
será aplicado um ajuste de 15% e para salários acima será 
apricado um reajuste de 10%
'''
salario = float(input('O salário do funcionário '))
percentagem = salario * 0.15

if salario >= 1250.0:
   percentagem = salario * 0.10
   print(f'O salário ficará R$ {salario+percentagem} ao final')
else:
   print(f'O salário ficará R$ {salario+percentagem} ao final')