'''
@Author Mateus R. Moreira
@Date 12/08/2019

Faça um programa que faça uma 
contagem regressiva para o estouro de fogos de artifício.
'''
from emoji import emojize
from time import sleep
loudspeaker = emojize(':loudspeaker:', use_aliases=True)
for c in range(1,11):
    print(f'{c}!!! {loudspeaker}')
    sleep(1)
print(f'Fireeee {emojize(":tada:", use_aliases=True)}')
