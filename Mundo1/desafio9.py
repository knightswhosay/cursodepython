'''
@author Mateus R. Moreira
@date 24/06/2019 
Peça um número e escreva sua tabuada de 0 - 10
'''
numero = int(input('Digite um número para calcular a sua tabuada '))

resultado = f'''
0  x  {numero} = {numero*0}
1  x  {numero} = {numero*1}
2  x  {numero} = {numero*2}
3  x  {numero} = {numero*3}
4  x  {numero} = {numero*4}
5  x  {numero} = {numero*5}
6  x  {numero} = {numero*6}
7  x  {numero} = {numero*7}
8  x  {numero} = {numero*8}
9  x  {numero} = {numero*9}
10 x  {numero} = {numero*10}
'''

print(resultado)