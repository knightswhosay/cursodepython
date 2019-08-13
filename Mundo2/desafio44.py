'''
@Author Mateus R. Moreira
@Date 11/08/2019

Elabore um programa que calculo o valor a ser pago 
Por um cliente em quantas parcelos e juros ou descontos

À vista / Cheque 10% de desconto  / à vista no cartão %5
Em cartão até 2 vezes proço do produto  / 3x ou mais 20% de juros  
'''
print('{:=^40}'.format('LOJAS CAQUI'))

valor = float(input('Valor da compra '))
parcelas = int(input('''
[1] Para pagar à vista ou em Cheque
[2] Para pagar à vista no cartão
[3] Para dividir em 2 vezes
[4] Para dividir em 3 ou mais vezes
'''))

parcelasqtd = int(input('Será quantas parcelas? '))
result = valor
if parcelas == 1:
   valor -= (valor*0.10)
   result = f'O valor à pagar com desconto será {valor}'
elif parcelas == 2:
   valor -= (valor*0.05)
   result = f'O valor à pagar com desconto será {valor}'
elif parcelas == 4:
    total = valor * 0.2

    result = 'Com um juros de 20% o tatal à se pagar será {}'.format(valor+total)
    
print('Os total das suas compras foram {} e {}'.format(valor,result))