'''
@author Mateus R. Moreira
@date 28/06/2019

Escreva um programa aplicador de multas
o limite de velocidade será 80km/h
aplique R$7,00 por cada quilômetro ultrapassado
'''
limite = 80
speed = int(input('velocidade do motorista? '))
ultrapassou = speed % limite

if ultrapassou >= 0:
  print(f'O motorista últrapassou {ultrapassou}KMs/H do limite de 80km\nreceberá uma múlta de {ultrapassou*7}R$')
print('Dirija com cuidado')


'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''