'''
<<<<<<< HEAD
@author Mateus R. Moreira
@date 03/07/2019

escreva um programa que calcule um aumento salarial

para salários acima de 1200 recebem um aumento de 10%
funcionários abaixo ou com o  salário igual à 1200 recebem 15%
'''
salario = float(input('Digite o salário para receber o reajuste R$ '))
aumento = (salario*0.15)+salario

if salario >= 1201:
    aumento = (salario*0.10)+salario

print(f'Reajuste salárial ficou em R${aumento}\nAntes era R${salario}')
'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''
=======
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
>>>>>>> 2acd11a67df51a9e057ab492aadbccc7aa0f4397
