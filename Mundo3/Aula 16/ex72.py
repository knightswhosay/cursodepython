'''
Faça uma tupla que tenha o tamanho completamente 
preenchida de 0 - 20
'''

# Variáveis do programa
extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze',
'quatorze ou catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

numero = input('Digite um número entra 0 e 20: ')


# Estruturas de decisão
while numero < 0 or numero > 20:
    numero = int(input('Ops! Tente novamente digite um número entre 0 e 20: '))

#Print Final
print(extenso[int(numero)])