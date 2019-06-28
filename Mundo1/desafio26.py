'''
@author Mateus R. Moreira
@date 27/06/2019

Peça uma frase pelo teclado 
E verifique quantas vezes aparece a letra A
Em que posição aparece a primeira e a última
'''
frase = str(input('Escreva um frase ')).lower()
howmany = frase.count('a')
first = frase.find('a')

print(f"""
A letra A aparece {howmany} vezes
A primeira letra A fica na posição {first+1}
A última letra aparece na posição {frase.rfind('a')+1}
""")

'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''