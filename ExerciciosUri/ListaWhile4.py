'''4) Implementar um programa que calcula o desconto previdenciário dos funcionários de uma empresa. O algoritmo deve,
dado um salário, retornar o valor do desconto proporcional ao mesmo.

- O cálculo de desconto segue a seguinte regra: o desconto deve ser de 11% do valor do salário,
entretanto, o valor máximo de desconto é R$320,00. Sendo assim, seu programa deve verificar se calculará sobre 11%  do salário ou utilizará o teto R$320,00.
No caso, de o desconto aplicado for R$320,00, seu programa deve indicar qual foi o % de desconto aplicado para este funcionário.

- Critério de parada definido pelo usuário (perguntar a cada verificação se deseja continuar)'''


while True:
    x = float(input('Qual seu salario?: '))
    desconto = x * 0.89
    y = x - desconto
    if y <= 320:
        print('Seu novo salário é', y)
    else:
        print('A porcentagem de desconto do seu salário foi',100 - (100*(x-320)/x) )
    h = input('Quer continuar? (Y/N)').upper()
    if h == 'Y':
        continue
    else:
        break
        
    

    
    
    

