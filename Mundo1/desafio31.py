'''
@author Mateus R. Moreira
@date 28/06/2019

escreva um programa que pergunte a distância de uma viagem
e escreva o preço da passagem cobrando R$0,50 para viagens de até 200km
e cobrando 0,45R$ para viagens mais longas
'''
quilometragem = int(input('Quantos quilômetros terá a tua viagem '))
preco = quilometragem*0.50
if quilometragem > 200:
   preco = quilometragem*0.45
print(f'O preço da sua viagem será R${preco}')
'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''