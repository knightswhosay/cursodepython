'''
@Author Mateus R. Moreira
30/07/2019

Faça um programa que calcule duas notas
de um aluna, segundo a sua média

Média abaixo de 5.0 Reprovador
Média entre 5.0 e 6.9 Recuperação
Média de 7 ou mais Aprovado
'''
nota1 = float(input('Primeiro Semestre '))
nota2 = float(input('Segundo Semestre '))
media = (nota1+nota2)/2
status = 'Em Recuperação'
result = 'Com a média {} O aluno está {}'.format(media,status)
if media <= 4.9:
   status = 'Reprovado(a)' 
   print(result.format(media,status))
elif media > 7.0:
    status = 'Aprovado(a)'
    print(result.format(media, status))
else:
    print(result.format(media, status))