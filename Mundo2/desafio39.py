'''
@Author Mateus R. Moreira
30/07/2019

Faça um programa que peça o ano de nascimento
Diga qual se ele ainda vai se alistar no serviço militar,
se é hora ou se já passou da hora.
'''
from datetime import datetime

anoNascimento = int(input('Ano de nascimento '))
idade = datetime.now().year - anoNascimento
faltam = 18 - idade
result = '''
Você está com {} anos de idade
E {} idade de se alistar {}
'''

if idade < 18:
    stre = f'faltam {faltam} anos para se alistar'
    print(result.format(idade,'ainda não está na', stre))
elif idade > 18:
    print(result.format(idade,'passou da ', ':)'))
else:
    print(result.format(idade,'está na', ':)'))