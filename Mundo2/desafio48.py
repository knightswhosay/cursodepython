'''
@Author Mateus R. Moreira
@Date 12/08/2019

Faça um programa que diga a soma de todos 
os números ímpares multiplos de 3 entre 1 e 500
'''
d = 0
a = 0
for c in range(1,501,2):
    print(c)
    if c%3==0:
        d+=c
        a+=1
print(f'A soma de todos os {a} números solicitados foram {d}')