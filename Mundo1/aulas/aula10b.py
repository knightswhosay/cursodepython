nota1 = float(input('Digite a nota do primeiro semestre '))
nota2 = float(input('Digite a nota do segundo semestre '))
m = (nota1+nota2)/2
resultado = 'Aluno está reprovado'

if m >= 6.0:
    resultado = 'Aluno está aprovado'
print(f'Com a média {m} o {resultado}')
