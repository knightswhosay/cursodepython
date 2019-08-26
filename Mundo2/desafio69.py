'''
@author Mateus R. Moreira
@date 22/08/2019

Escreva um programa que peça e leia
a idade de várias pessoas e diga 
quantas pessoas tem mais de 18 anos

quantos homens foram cadastrados
e quantas mulheres tem menos de 20 anos
'''
nome  = str(input('Digite o nome  da pessoa: '))
idade = int(input('Digite a idade da pessoa: '))
sexo  = str(input('Digite o sexo  da pessoa [M/F] '))
r = ''
mulheresmenores = 0
homens = 0
maior = 0
while r != 'n':
    if sexo == 'f' and idade < 20:
       mulheresmenores += 1
    elif sexo == 'm':
       homens += 1 
    else:
       sexo  = str(input('Digite uma resposta válida para o sexo [M/F] ')) 

    if idade > 18:
       maior += 1  
    nome  = str(input('Digite o nome  da pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))
    sexo  = str(input('Digite o sexo  da pessoa [M/F] '))
    r = str(input('Quer continuar? [S/n] ')).lower()
print(f'''
Foram cadastrados
{maior} maiores de idade  18 >
{mulheresmenores} mulheres com menos de 20 anos
{homens} homens
''')