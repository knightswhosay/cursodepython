'''
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