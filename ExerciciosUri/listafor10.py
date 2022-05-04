'''10) Considerar uma turma da Disciplina de Cálculo I, com 5 alunos, fazer um
programa que:
10.1) Calcule a média das notas;
10.2) Indique o nome do aluno com a média mais alta
10.3) Informe seu conceito (Aprovado, Em Recuperação, Reprovado).
Considerando que essas regras funcionam da mesma forma que na UFSC:
se a média for 5.75 ou maior, o aluno está aprovado, se a nota for maior
ou igual a 2.75, ele tem o direito de fazer a prova de recuperação e se o
aluno obtiver uma média menor que 2.75 ele foi reprovado.'''

notas = 0
media_alta = -1
for x in range(5):
    y = float(input('Digite as medias dos alunos: '))
    if y > 5.75:
        print('Aprovado')
    elif y >= 2.75:
        print('Direito a recuperação')
    else:
        print('Reprovado')
    notas += y
    h = notas/5
    if y > media_alta:
        media_alta = y
print('Média geral: ', h)
print('Media mais alta: ',media_alta)
    
    
