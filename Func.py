nome = (input('Qual o nome do aluno?'))
x = float(input('Qual a nota do aluno?'))

if x >= 7:
      situacao = 'Está de APROVADO'
elif x >= 5 :
    situacao = 'Está de RECUPERAÇÃO'
else:
    situacao = 'Está REPROVADO'

print(f'{nome} {situacao}')