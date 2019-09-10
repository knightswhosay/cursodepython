'''
@author Mateus R. Moreira
@date 22/08/2019

Crie um programa que simule um caixa eletrônico
peça o quanto quer sacar e as cédulas

50, 20, 10, 1 
'''
print('='*30)
print(f'{"BANCO CEV":^30}')
print('='*30)
valor = int(input('Quanto você quer sacar? R$ '))
total = valor
ced = 50
totalced = 0
while True:
   if total >= ced:
     total -= ced
     totalced += 1
   else:
     print(f'O total de {totalced} Cédulas de R${ced}')
     if ced == 50:
         ced = 20
     elif ced == 20:
          ced = 10
     elif ced == 10:
           ced = 1
     totalced = 0
     if total == 0:
        break