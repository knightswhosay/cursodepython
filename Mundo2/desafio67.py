'''
@author Mateus R. Moreira
@date 19/08/2019

Escreva um programa
que mostre a tabuada de qualquer número
ele só para e o número for negativo
'''
print(f'-'*30)
n = int(input('Você quer ver a tabuada de que número? '))
if n < 0:
    print(':> Programa Tabuada encerrado Bye ;)') 
while n > 0:
    print(f'''
{n}  x  1  {n*1}
{n}  x  2  {n*2}
{n}  x  3  {n*3}
{n}  x  4  {n*4}
{n}  x  5  {n*5}
{n}  x  6  {n*6}
{n}  x  7  {n*7}
{n}  x  8  {n*8}
{n}  x  9  {n*9}
{n}  x  10 {n*10}
''')
    n = int(input('Você quer ver a tabuada de que número? '))
    if n < 0:
       print(':> Programa Tabuada encerrado Bye ;)') 
       break 