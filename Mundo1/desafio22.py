'''
@author Mateus R. Moreira
@date 26/06/2019

Crie um programa que leia o nome completo
de uma pessoa e mostre

1 O nome completo com todas as letras maíscula
2 O nome com todas as letras minusculas
3 Quantas letras tem ao todo sem considorar os espaços
'''
nome = str(input('Escreva seu nome completo '))
comsplit =  nome.split()
maiusculo = nome.upper()
minusculo = nome.lower()
semespaco = len(''.join(comsplit))
letrsprimeira = len(comsplit[0])


print(f"""
Seu nome é {nome}

Todo em maísculo fica {maiusculo}
Todo em minusculo fica {minusculo}
O total de letras são {semespaco}
O total de letras so seu primeiro nome é {letrsprimeira}
""")



'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''