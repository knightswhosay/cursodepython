'''
@author Mateus R. Moreira
@date 27/06/2019

Crio um programa que leia o 
nome de uma pessoa e verifique se tem silva no nome
'''
nome = str(input('Escreva seu nome ')).strip()
nome = nome.lower()
print(f'Silva aparece {nome.count("silva")} vezes no seu nome')



'''
Info: Estes exercícios são tirados do
curso em video de python. 
'''