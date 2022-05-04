'''5) Florianópolis é uma cidade que possui diversas praias.
De forma a melhor orientar os turistas a Secretaria Municipal de Turismo mediu a distância de cada praia a partir do centro da cidade.
Seu programa deve solicitar que o usuário indique o número de praias que deseja cadastrar. E para cada praia, indique o nome (string) e a distância do centro da cidade (int).
A partir destas informações, seu programa deve obter os seguintes dados:
•   qual a praia mais distante do centro da cidade;
•   quantas praias estão entre 15 e 20 km do centro;
•  qual a distância média das praias (arredondado na primeira casa decimal);
'''

distancia = -1
nome = ''
media = 0
contagem = 0
h = 0
praias = 0
x = int(input('Digite o numero de praias que quer cadastrar: '))
while x > 0:
    y = input('Qual o nome da praia?: ')
    h = float(input('Qual a distancia do centro da cidade?: '))
    media += h
    if h >= 15 and h <= 20:
        praias += 1
    if h > distancia:
        distancia = h
        nome = y
    x -= 1
    contagem += 1
print('A mais distante é a praia: ', nome.capitalize())
print(praias,' praias estão entre 15 a 20km do centro')
print('A media é', media/contagem)
    
    
    

    
    
    
    

