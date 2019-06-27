'''
@author Mateus R. Moreira
@date 26/06/2019

Escreva um programa que pergunte a quantidade de Km percorridos 
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, 
sabendo que o carro custa R$60 
por dia e R$0,15 por Km rodado.
'''
dias = int(input('Por quantos Dias que o carro foi alugado? '))
km = float(input('Quantos KM foram percorridos? '))
aluguel = (dias * 60)+(km * 0.15)

print(f'O carro foi alugado por {dias} pagando R$60 P/dia\nCom {km} Quilômetros rodoados por R$0,15 Centavos cada Quilômetros dá um total de R${aluguel}')




'''
Info: Estes exercícios são tirados do 
curso em video de python. 
'''