'''
Aula que ensina o uso de Módulos
'''
import math
import emoji

num = int(input('Digite um número e veja sua raiz quadrada: '))
raizquadrada = math.sqrt(num)

print(f'A raíz quadrade de {num} 🌍 é igual a {math.ceil(raizquadrada):.2f}', emoji.emojize(' :shit:', use_aliases=True))