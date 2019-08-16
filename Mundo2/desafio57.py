'''
@author Mateus R. Moreira
@date 17/09/2019

escreva um programa que peça o sexo de uma pessoa
somente é aceito F para feminino e M para masculino
'''
s = input('Escreva o seu sexo [F/M] ').strip().lower()
sexo = ['m', 'f']
while s not in sexo:
    s = input('''
Por favor digite F para faminino e 
M para masculino ''').lower()

print(f'Obrigado pessoa do sexo {s}')