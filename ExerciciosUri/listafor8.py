'''8) Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles. No final mostre a soma dos
números (do intervalo).'''

x = int(input('Digite um numero: '))
y = int(input('Digite outro numero: '))
h = 0
for i in range(x,y+1):
    h += i
print(h)
    
