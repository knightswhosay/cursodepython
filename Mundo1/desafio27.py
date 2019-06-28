'''
@author Mateus R. Moreira
@date 27/06/2019

Faça um programa que leia o nome completo 
de uma pessoa e escreva o primeiro nome
Segundo e último
'''
nome = str(input('Escreva seu nome completo '))
nome = nome.split()

print(f"Primeiro Nome {nome[0]}\núltimo Nome {nome[-1]}")

'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''