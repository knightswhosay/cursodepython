'''
@author Mateus R. Moreira
@date 13/09/2019
Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
'''
from datetime import datetime
maior, menor = 0,0

for n in range(1,8):
    n = int(input(f'Digite o ano de nascimento da {n}° pessoa '))
    n = datetime.now().year - n
    if n >= 18:
        maior += 1
    else:
        menor +=1

print(f'''
Temos {maior} pessoas maior de idade

E temos {menor} menor de idade
''')