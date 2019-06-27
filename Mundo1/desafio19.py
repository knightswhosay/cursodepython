'''
@author Mateus R. Moreira
@date 26/06/2019

Um professor quer sortear
um dos seus alunos para apagar o quadro.
Ele vai escolher aleatoriamente 
'''
from random import randint

alunos = ['João', 'Maria', 'Pedrinho', 'Joaquina']
escolhido = alunos[randint(0,3)]

print(f'Quem vai apagar o quadro será {escolhido}')


'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''