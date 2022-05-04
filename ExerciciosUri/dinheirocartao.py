produto = float(input('Preco: '))
print('Dinheiro  [D]')
print('Cartão 1x [1x]')
print('Cartão 2x [2x]')
print('Cartão 3x [3x]')
pagamento = input('Tipo de pagamento: ')

if pagamento.upper() == 'D':
    print(produto * 0.9)
elif pagamento.upper() == '1x':
    print(produto * 0.95)
elif pagamento.upper() == '2x':
    print(produto)  
elif pagamento.upper() == '3x':
    print(produto * 1.2)
else:
    print('Tipo de pagamento inválido!')

