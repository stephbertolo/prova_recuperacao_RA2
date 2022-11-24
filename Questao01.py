alunos = list()
notas = list()

for aluno in range(5):
    nomeAluno = str(input('Digite o nome do aluno: '))
    alunos.append(nomeAluno)

for aluno in alunos:
    notaAluno = float(input(f'Digite a nota do aluno {aluno} entre 0 e 10: '))
    notas.append(notaAluno)


for aluno in alunos:
    if notaAluno >= 7:
        print(f"{aluno} foi aprovado(a) com nota {notaAluno}")

    elif 4 < notaAluno < 6.9:
        print(f'{aluno} está em recuperação com nota {notaAluno}')

    else:
        print(f'{aluno} foi reprovado com nota {notaAluno}')

