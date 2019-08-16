'''
@author Mateus R. Moreira
@date 15/09/2019

Escreva um programa que leia o nome idade, e sexo 
de quatro pessoas no final do programa diga 
Qual a média de idade do grupo
Qual é o homem mais velho 
E quantas mulheres tem menos de 20 anos
'''

'''
Variaveis relacionadas ao processo
'''
maisvelho = [0, '']
media = 0
mulheres = 0

for i in range(1,5):
    print(f'==== {i}° Pessoa ====')
    '''
    Variaveis relacionado a pessoa
    '''
    nome = str(input('Qual é o Nome da pessoa: '))
    idade = int(input('Qual é a idade: '))
    sexo = str(input('Sexo ')).lower()
    
    #analize area
    media += idade
    if idade > maisvelho[0] and sexo == 'm':
       maisvelho[0] = idade
       maisvelho[1] = nome
    if idade < 20 and sexo == 'f':
        mulheres += 1

print(f"A média de idade do grupo é {media/4:.2f}")
print(f'O homem mais velho se chama {maisvelho[1]} e tem {maisvelho[0]} anos')
print(f'E tem {mulheres} com menos de 20 anos')