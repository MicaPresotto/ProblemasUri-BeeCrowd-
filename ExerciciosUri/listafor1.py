'''1) Escreva um programa que imprima todos os anos bissextos do século XXI.
Lembre-se que o primeiro ano bissexto do século foi em 2004 e que o último será
em 2096 e que os anos bissextos ocorrem usualmente de 4 em 4 anos'''

calculo = (2004 % 4 == 0 and 2004 % 100 != 0) or (2004 % 400 == 0)
for x in range(2004,2097):
    if x % 4 == 0:
        print(x)
    else:
        pass

