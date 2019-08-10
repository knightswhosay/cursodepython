'''
@author Mateus R. Moreira
31/07/2019

Faça um programa que leia a idade de um atleta
e diga de que categoria ele é

Até 9 anos Mirim   Até 19 Junior
até 14 Infantil    Até 25 Sênior
Acima de 25 Master
'''
from datetime import datetime
anodenascimento = int(input('Qual é o ano de nascimento do Atleta? '))
idade = datetime.now().year - anodenascimento
result = '''
Atleta na idade de {} anos
está na categoria {}
'''
categoria = 'Master'
if idade <= 9:
   categoria = 'Mirim' 
   print(result.format(idade,categoria)) 
elif 9 < idade <= 14:
   categoria = 'Infantil' 
   print(result.format(idade,categoria))
elif 14 < idade <= 19:
   categoria = 'Junior' 
   print(result.format(idade,categoria))
elif 19 < idade <= 24:
   categoria = 'Sênior' 
   print(result.format(idade,categoria))
elif idade > 40:
   categoria = 'Lenda' 
   print(result.format(idade,categoria))    
else:
   print(result.format(idade,categoria))
