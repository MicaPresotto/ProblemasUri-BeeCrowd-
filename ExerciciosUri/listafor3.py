'''3) Uma universidade particular oferece um desconto de 30% na mensalidade do
aluno com melhor nota (média geral). Implemente um programa que após
receber as informações do aluno (nome, nota/média geral, valor mensalidade)
verifique quem é o aluno com melhor nota e calcule o desconto de sua
mensalidade.
Ao final de sua execução, o programa deve mostrar:
- o nome do aluno com melhor nota,
- o valor da mensalidade (sem desconto) e
- o valor da mensalidade com o desconto e 30%;
Considerar 5 alunos (as informações devem ser lidas do teclado).'''


maior_nota = -1
nome_do_aluno = ''
valor_facul = ''
for x in range(5):
    nome = input('Nome do aluno: ')
    nota = float(input('Média geral: '))
    valor = float(input('Valor da mensalidade: '))
    if maior_nota < nota:
        maior_nota = nota
        float(maior_nota)
        nome_do_aluno = nome
        valor_facul = valor
    else:
        continue
    
print('Aluno: ', nome_do_aluno)
print('Valor: ',valor_facul)
print('Valor com desconto: ',valor_facul*0.7)