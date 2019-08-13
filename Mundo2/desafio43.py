'''
@Author Mateus R. Moreira
@Date 11/08/2019

Faça um programa que calcula o IMC
'''

peso = float(input('Qual é o teu peso? (KG) '))
altura = float(input('Qual é a tua altura? (M) '))
result = ''
imc = peso / (altura ** 2)

if 18.5 <= imc < 25:
    result = 'Peso ideal'
elif 25 < imc < 30:
    result = 'Acima do peso '
elif 30 < imc < 40:
    result = 'Obeso '
elif imc > 40:
    result = 'Obesidade móbida'
else:
   result = 'Abaixo do peso'

print(f'O seu IMC é {imc:.0f} Você está {result}')