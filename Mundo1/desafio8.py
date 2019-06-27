'''
@author Mateus R. Moreira
@date 24/06/2019
Escreva um programa que peça um valor em metros
e exiba convertido em centímetros e milímitros
'''

metros = float(input('Escreva o tamanho em metros '))
centimetros = metros*100
milimetros = metros*1000

print(f'{metros:.2}M == {centimetros}CM\n{metros}M == {milimetros}MM')