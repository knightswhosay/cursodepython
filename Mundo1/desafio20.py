'''
@author Mateus R. Moreira
@date 26/06/2019

Faça um programa da 
ordem de apresentar um trabalho
'''
from random import shuffle
alunos1 = str(input('Primeiro Aluno '))
alunos2 = str(input('Segundo Aluno '))
alunos3 = str(input('Terceiro Aluno '))
alunos4 = str(input('Quarto Aluno '))
alunos = [alunos1,alunos2,alunos3,alunos4]
shuffle(alunos)
print(f'A ordem será {alunos}')
'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''