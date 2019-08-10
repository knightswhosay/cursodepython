'''
@author Mateus R. Moreira
@date 29/07/2019
Faça um programa para aprovar o empréstimo bancário
O programa pede o valor da casa, O salário da 
pessoa que quer comprar
E quantos anos

Se a prestação for menos que 30% do valor da casa
Será aprovada caso o contrário será reprovada
'''

## Variáveis
vcasa = float(input('Qual é o valor da casa? '))
vsalario = float(input('Qual é o salário do comprador? '))
anos = int(input('Para pagar em quantos anos? '))
vprestacao = (vcasa / anos) / 12
status = ''
limite = vsalario*0.3
result = '''
O crédito foi {}
Com o valor da parcela será {:.2f}
Para pagar em {} Anos
'''

if vprestacao <= limite:
    status = 'Aprovado'
    print(result.format(status,vprestacao, anos))
elif vprestacao > limite:
    status = 'Reprovado'    
    print(result.format(status,vprestacao, anos))
