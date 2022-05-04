'''1) Escreva um programa que leia o sexo das pessoas, mas somente aceite “M” ou “F”.
Caso esteja errado, peça a digitação novamente até ter um valor correto'''

while True:
    x = input('Digite seu sexo: ').upper()
    if x =='M' or x == 'F':
        break
    else:
        print('Erro! Digite novamente')
        continue