'''
@author Mateus R. Moreira
@date 30/07/2019

faça um programa que leia um número inteiro e 
converta nas bases de conversão

1 - Biário
2 - octal
3 - hexadecimal
'''

num = int(input('Digite um número inteiro '))
result = '''
O número {} na base {}
fica {}
'''
swinum = int(input('''
Escolha uma base
1 - Biário
2 - octal
3 - hexadecimal
'''))

if swinum == 1:
    print(result.format(num,"Binária",bin(num)))
elif swinum == 2:
    print(result.format(num,"octadecimal",oct(num)))
else:
    print(result.format(num,"hexadecimal",hex(num)))    