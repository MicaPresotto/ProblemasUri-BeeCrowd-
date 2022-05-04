'''2) Implemente um jogo onde o usuário deve adivinhar o número escolhido pelo computador (entre 0 e 10).
O Usuário irá digitando valores até descobrir este valor.
Quando o usuário “acertar”, uma mensagem avisa o final do jogo (que o número correto foi digitado) e o número de tentativas.'''
from random import randrange
x = randrange(11)
contagem = 0
while True:
    contagem += 1
    y = int(input('Advinhe o valor: '))
    if y != x:
        print('Quase lá')
    else:
        print('Voce acertou!')
        break

print('Numero de tentativas foi:',contagem)
    

