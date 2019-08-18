'''
@author Mateus R. Moreira
@date 17/09/2019

Escreva um programa que peça dois números 
e exiba um menu de operações
'''
n1 = float(input('Digite o primeiro número '))
n2 = float(input('Digite o segundo número '))
g = 0

while g != 5:
  g = int(input(f'''
Qual operação você quer fazer?
[1] Somar
[2] Multiplicar
[3] Qual é o maior
[4] novos números
[5] Sair 
'''))
  if g == 1:
   print(f'A soma de {n1} + {n2} = {n1+n2}')
  
  elif g == 2:
    print(f'A multiplicação de {n1} x {n2} = {n1*n2}') 
  elif g == 3:
     if n1 > n2:
        print(f'{n1} é o maior')
     else:   
        print(f'{n2} é o maior')
  elif g == 4:
    n1 = float(input('Digite o primeiro número '))
    n2 = float(input('Digite o segundo número '))
  elif g == 5:
    print(':> Bye')
  else:
    print('Opção inválida')          
