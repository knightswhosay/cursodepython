'''
@author Mateus R. Moreira
@date 24/06/2019

Faça um programa que peça o tamanho de uma parede
e calcule a quantidade de tinta necessária para pintá-la
sabendo que para cada litro de tinta pinta uma área de 2M²

Marca da Tinta Tatu® é meramente ficticia 
'''

altura = float(input('Digite altura da parede em M: '))
largura = float(input('Digite largura da parede em M: '))
metroaoquadrado = altura*largura

print(f'Sua parede de {metroaoquadrado}M² precisará de {metroaoquadrado/2:.2f} litros de tinta Tatu®')