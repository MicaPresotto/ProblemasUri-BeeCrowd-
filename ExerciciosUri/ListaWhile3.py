'''3)  Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos e qual foi o maior e o menor valor lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

media = 0
contador = 0
while True:
    x = float(input('Digite um numero para fazer a media: '))
    media += x
    contador += 1
    y = input('Voce deseja continuar digitando numeros?(Y/N) :').upper()
    if y == 'Y':
        continue
    else:
        print(' A media é', media/contador)
        break
        
    
    
    

