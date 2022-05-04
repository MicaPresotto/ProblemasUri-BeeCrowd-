'''7) Faça um programa que peça para n pessoas a sua idade (o valor de n será
solicitado ao usuário), ao final o programa deverá verificar se a média de idade
da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é
jovem, adulta ou idosa, conforme a média calculada.'''

n = int(input('Digite o numero de pessoas: '))
idade = 0
for x in range (n):
    y = int(input('Digite a idade: '))
    idade += y
h = idade/n
print(h)
if h >= 0 and h <= 25:
    print('Jovens')
elif h > 25 and h <= 60:
    print('Adultos')
else:
    print('Idosos')
