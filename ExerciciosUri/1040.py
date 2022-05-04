w, x, y, z = [float(x) for x in input().split()]


n1 = w*2
n2 = x*3
n3 = y*4
n4 = z*1
media = (n1+n2+n3+n4)/10
if media >= 7:
    print('Aluno aprovado')
elif media < 5:
    print('Aluno reprovado')
elif media > 5 and media < 6.9:
    print('Aluno em exame')
    exame = float(input('Nota do exame: '))
    h = (exame + media)/2
    if h >= 5:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')
    print('Média final', h)
